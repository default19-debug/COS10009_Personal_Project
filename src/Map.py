import pygame
from Setting import *
class Map:
    def __init__(self):
        self.grid = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
            [1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
    def Has_wall_at(self, x, y):
        if x < 0 or x >= WindowWidth or y < 0 or y >= WindowHeight:
            return True
        grid_x = int(x // TileSize)
        grid_y = int(y // TileSize)
        return self.grid[grid_y][grid_x] == 1

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
