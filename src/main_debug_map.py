
import pygame
from Setting import *
from Map import *
from Player import *
from Rays import *
from Raycaster import*
Screen = pygame.display.set_mode((WindowWidth, WindowHeight))

map = Map()
player = Player()
raycaster = Ratcaster(player,map)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    Screen.fill((0,0,0))

    map.Render(Screen)
    player.render(Screen)
    player.update()
    raycaster.Castallrays(Screen)
    raycaster.render(Screen)
    pygame.display.update()







