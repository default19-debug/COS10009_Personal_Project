
import pygame
from Setting import *
from Map import *
from Player import *
from Rays import *
from Raycaster import*
from Anubis import *
Screen = pygame.display.set_mode((WindowWidth, WindowHeight))
print(Total_debug_hours)
map = Map()
player = Player(map)
anubis = Anubis(100, 100, map, player)
raycaster = Raycaster(player,map)
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
    anubis.render(Screen)
    anubis.update()
    pygame.display.update()








