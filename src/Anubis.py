import pygame
import math
from Setting import *
from collections import deque


class Anubis:
    def __init__(self, start_x, start_y, game_map, player):
        self.x = start_x
        self.y = start_y
        self.radius = 5
        self.speed = 1

        self.game_map = game_map
        self.player = player

        self.path = []  # This will store the list of (grid_x, grid_y) coordinates to follow

        self.image = pygame.image.load('image.png').convert_alpha()
        self.state = "HUNTING"
        self.enrage_start_time = 0

    def get_grid_pos(self, x, y):
        """Converts raw (x, y) coordinates into grid [row][col] indices."""
        col = int(x // TileSize)
        row = int(y // TileSize)
        return col, row

    def find_path_bfs(self):
        """Finds the shortest path from Anubis to the Player using Breadth-First Search."""
        anubis_grid = self.get_grid_pos(self.x, self.y)
        player_grid = self.get_grid_pos(self.player.x, self.player.y)

        queue = deque([anubis_grid])
        visited = {anubis_grid}
        came_from = {anubis_grid: None}

        while queue:
            current = queue.popleft()

            if current == player_grid:
                break

            col, row = current
            neighbors = [
                (col, row - 1),  # Up
                (col, row + 1),  # Down
                (col - 1, row),  # Left
                (col + 1, row)  # Right
            ]

            for n_col, n_row in neighbors:

                if 0 <= n_row < len(self.game_map.grid) and 0 <= n_col < len(self.game_map.grid[0]):


                    if self.game_map.grid[n_row][n_col] != 1 and (n_col, n_row) not in visited:
                        queue.append((n_col, n_row))
                        visited.add((n_col, n_row))
                        came_from[(n_col, n_row)] = current

        self.path = []
        current = player_grid

        if current in came_from:
            while current != anubis_grid:
                self.path.append(current)
                current = came_from[current]

            self.path.reverse()

    def update(self):
        self.find_path_bfs()

        # Get our current grid positions
        anubis_col, anubis_row = self.get_grid_pos(self.x, self.y)
        player_col, player_row = self.get_grid_pos(self.player.x, self.player.y)

        if anubis_col == player_col and anubis_row == player_row:
            angle = math.atan2(self.player.y - self.y, self.player.x - self.x)
            self.x += math.cos(angle) * self.speed
            self.y += math.sin(angle) * self.speed

        elif len(self.path) > 0:
            target_col, target_row = self.path[0]

            target_x = (target_col * TileSize) + (TileSize / 2)
            target_y = (target_row * TileSize) + (TileSize / 2)

            dist_to_target = math.sqrt((target_x - self.x) ** 2 + (target_y - self.y) ** 2)

            if dist_to_target < 2:
                self.path.pop(0)
            else:
                angle = math.atan2(target_y - self.y, target_x - self.x)
                self.x += math.cos(angle) * self.speed
                self.y += math.sin(angle) * self.speed

        dist_to_player = math.sqrt((self.player.x - self.x) ** 2 + (self.player.y - self.y) ** 2)
        if dist_to_player < (self.radius + self.player.radius):
            print("JUMPSCARE! YOU DIED!")
            return True

        return False



    def render_25D(self, screen, z_buffer):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance < 1:
            distance = 1

        sprite_angle = math.atan2(dy, dx)
        delta_angle = sprite_angle - self.player.RotateAngle

        while delta_angle < -math.pi:
            delta_angle += 2 * math.pi
        while delta_angle > math.pi:
            delta_angle -= 2 * math.pi


        if abs(delta_angle) > (FOV / 2) + 0.2:
            return


        screen_x = (WindowWidth / 2) + (math.tan(delta_angle) * 350)
        sprite_size = int((35 / distance) * 350)

        scaled_img = pygame.transform.scale(self.image, (sprite_size, sprite_size))

        light_level = int(255 * (20 / distance))
        light_level = min(255, max(0, light_level))

        tint = pygame.Surface((sprite_size, sprite_size))
        tint.fill((light_level, light_level, light_level))
        scaled_img.blit(tint, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
        start_x = int(screen_x - sprite_size / 2)
        end_x = int(screen_x + sprite_size / 2)
        draw_y = (WindowHeight / 2) - (sprite_size / 2) + self.player.walk_offset

        for stripe in range(start_x, end_x):
            # Check 1: Is this specific pixel column actually on the screen?
            if 0 <= stripe < WindowWidth:
                # Check 2: The Z-Buffer! Is Anubis closer than the wall at this exact pixel?
                if distance < z_buffer[stripe]:
                    # Draw a 1-pixel wide, vertically scaled slice of the purple rectangle
                    image_col = stripe - start_x
                    screen.blit(scaled_img, (stripe, draw_y), (image_col, 0, 1, sprite_size))