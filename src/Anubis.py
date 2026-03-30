import pygame
import math
from Setting import *

class Anubis:
    def __init__(self, start_x, start_y, game_map, player):
        self.x = start_x
        self.y = start_y
        self.radius = 5
        self.speed = 1

        self.game_map = game_map
        self.player = player

        self.path = []  # This will store the list of (grid_x, grid_y) coordinates to follow

        # TODO: Add a timer or cooldown variable so BFS doesn't run every single frame (saves CPU)

    def get_grid_pos(self, x, y):
        """Converts raw (x, y) coordinates into grid [row][col] indices."""
        # TODO: Divide the x and y by TileSize and cast to an integer to find the grid position.
        pass

    def find_path_bfs(self):
        """Finds the shortest path from Anubis to the Player using Breadth-First Search."""
        anubis_grid = self.get_grid_pos(self.x, self.y)
        player_grid = self.get_grid_pos(self.player.x, self.player.y)

        # 1. Setup your Queue for BFS and a 'visited' set to avoid looping
        # 2. Setup a dictionary to keep track of where you came from (for backtracking the path)

        # TODO: Implement the BFS loop
        # - Pop the current node from the queue
        # - Check if it's the player_grid position (Target found!)
        # - If not, check Neighbors (Up, Down, Left, Right)
        # - Ensure neighbors aren't walls (self.game_map.grid[row][col] == 1) and haven't been visited.
        # - Add valid neighbors to the queue.

        # TODO: Backtrack from the player_grid using your dictionary to build the self.path list.
        # - Reverse the list so the first item is the very next step Anubis needs to take.
        pass

    def update(self):
        """Handles Anubis's movement and logic every frame."""
        # TODO: Check if we need to recalculate the path (e.g., run find_path_bfs() every 0.5 seconds)

        # TODO: Movement Logic
        # - If self.path has coordinates, look at the first target coordinate.
        # - Convert that grid coordinate back into a center pixel coordinate (x, y).
        # - Calculate the angle between Anubis's current (self.x, self.y) and the target.
        # - Use math.cos() and math.sin() to move self.x and self.y towards the target.

        # TODO: Reached Node Check
        # - If Anubis is super close to the current target node, pop it from self.path so he targets the next one.

        # TODO: Kill Condition
        # - Calculate the distance between Anubis and the Player.
        # - If distance < (self.radius + self.player.radius), return a "GAME OVER" or "JUMPSCARE" flag.
        return False  # Return True if the player is caught!

    def render(self, screen):
        """Draws Anubis on the 2D debug map."""
        # A terrifying purple dot
        pygame.draw.circle(screen, (138, 43, 226), (int(self.x), int(self.y)), self.radius)

        # Optional TODO: Draw the BFS path as a line so you can visually verify he's thinking correctly!