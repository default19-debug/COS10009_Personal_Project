import pygame
import math
from Setting import *
from Map import *

class Player:
    def __init__(self,game_map):
        self.x = (1 * TileSize) + (TileSize / 2)
        self.y = (1 * TileSize) + (TileSize / 2)
        self.radius = 3

        self.RotateAngle = 0
        self.turnDireciton = 0
        self.walkDirection = 0

        self.movespeed = 1
        self.Rotatespeed = 1

        self.mouse_sens = 0.001
        pygame.mouse.get_rel()
        self.hitbox_x = 0
        self.hitbox_y = 0

        self.new_x=0
        self.new_y=0
        self.game_map = game_map
    def update(self):
        self.turnDireciton = 0
        self.walkDirection = 0

        keys = pygame.key.get_pressed()


        mx, my = pygame.mouse.get_rel()
        self.turnDireciton = mx * self.mouse_sens
        self.RotateAngle += self.turnDireciton * self.Rotatespeed
        movestep = 0
        if keys[pygame.K_w]:
            movestep = self.movespeed
        if keys[pygame.K_s]:
            movestep = -self.movespeed


        dx = math.cos(self.RotateAngle) * movestep
        dy = math.sin(self.RotateAngle) * movestep

        if keys[pygame.K_d]:
            dx += math.cos(self.RotateAngle + math.pi/2) * self.movespeed
            dy += math.sin(self.RotateAngle + math.pi/2) * self.movespeed
        if keys[pygame.K_a]:
            dx += math.cos(self.RotateAngle - math.pi/2) * self.movespeed
            dy += math.sin(self.RotateAngle - math.pi/2) * self.movespeed
        new_x = self.x + dx
        new_y = self.y + dy
        self.hitbox_x = new_x + (5 if dx > 0 else -5)
        self.hitbox_y = new_y + (5 if dy > 0 else -5)

        if (self.game_map.grid[int((self.y - 5) / TileSize)][int(self.hitbox_x / TileSize)] in [0,2] and
                self.game_map.grid[int((self.y + 5) / TileSize)][int(self.hitbox_x / TileSize)] in [0,2]):
            self.x = new_x

        if (self.game_map.grid[int(self.hitbox_y / TileSize)][int((self.x - 5) / TileSize)] in [0,2] and
                self.game_map.grid[int(self.hitbox_y / TileSize)][int((self.x + 5) / TileSize)] in [0,2]):
            self.y = new_y


        current_grid_x = int(self.x // TileSize)
        current_grid_y = int(self.y // TileSize)


        if self.game_map.grid[current_grid_y][current_grid_x] == 2:
            return True

        return False  # Game continues
    def render(self, screen):
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), self.radius)
        pygame.draw.line(
            screen,
            (200,0,0),
            (self.x, self.y),
            (self.x + 40 * math.cos(self.RotateAngle),
             self.y + 40 * math.sin(self.RotateAngle))
        )
