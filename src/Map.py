import pygame
import random
import json
import os

from Setting import *
class Map:
    def __init__(self):
        map_number = random.randint(1, 5)
        filename = f"Maps_files/map_{map_number}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.grid = json.load(file)
            print(f"Successfully loaded {filename}")
        else:
            print(f"Warning: {filename} not found. Loading default map.")


        self.exit_row = 0
        self.exit_col = 0
        self.spawn_exit()


    def spawn_exit(self):
        available_spots = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == 0 and not (row == 1 and col == 1):
                    available_spots.append((row, col))
        if len(available_spots) > 0:
            chosen_spot = random.choice(available_spots)
            self.exit_row = chosen_spot[0]
            self.exit_col = chosen_spot[1]
            self.grid[self.exit_row][self.exit_col] = 2

            print(f"Exit spawned at grid: Row {self.exit_row}, Col {self.exit_col}")

    def Has_wall_at(self, x, y):
        if x < 0 or x >= WindowWidth or y < 0 or y >= WindowHeight:
            return True
        grid_x = int(x // TileSize)
        grid_y = int(y // TileSize)
        return self.grid[grid_y][grid_x] != 0

    def Get_wall_type(self, x, y):
        if x < 0 or x >= WindowWidth or y < 0 or y >= WindowHeight:
            return 1
        grid_x = int(x // TileSize)
        grid_y = int(y // TileSize)
        return self.grid[grid_y][grid_x]

    def Render(self,screen):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                tile_x = j * TileSize
                tile_y = i * TileSize

                if self.grid[i][j] == 0:
                    pygame.draw.rect(screen , (255,255,255), (tile_x,tile_y,TileSize-1,TileSize-1))
                elif self.grid[i][j] == 1:
                    pygame.draw.rect(screen , (40,40,40), (tile_x,tile_y,TileSize-1,TileSize-1))
                    #tile size are minus by 1 so I can see the grid in the map
                elif self.grid[i][j] == 2:
                    pygame.draw.rect(screen, (0, 100, 255), (tile_x, tile_y, TileSize - 1, TileSize - 1))
