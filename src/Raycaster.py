import pygame
import math
from Rays import Ray
from Setting import*
from Map import *
class Raycaster:
    def __init__(self,player,Map):
        self.ray=[]
        self.player = player
        self.Map = Map
    def Castallrays(self,screen):
        self.ray=[]
        rayAngle = (self.player.RotateAngle - FOV/2)
        for i in range(NRays):
            ray = Ray(rayAngle,self.player,self.Map)
            ray.cast(screen)
            self.ray.append(ray)
            rayAngle += FOV/NRays

    def render(self,screen):

        for ray in self.ray :
            ray.render(screen)


    def render_25D(self,screen):
        self.z_buffer = []
        for ray in self.ray:
            self.z_buffer.append(ray.distance)
        i =0 #this is the counter, im setting it as i for the sake of debugging.
        for ray in self.ray :
            line_height = (35 / ray.distance) * 350
            draw_begin =(WindowHeight / 2) - (line_height / 2) + self.player.walk_offset
            draw_end = line_height


            if ray.wall_type == 2:
                pygame.draw.rect(screen, (0, 100, 255), (i * RES, draw_begin, RES, draw_end))
            else:
                c = min(255, max(0, int(ray.color)))
                pygame.draw.rect(screen, (c, 0, 0), (i * RES, draw_begin, RES, draw_end))
            #pygame.draw.rect(screen,(ray.color,ray.color,ray.color) , (i*RES,draw_begin,RES,draw_end))
            i +=1
