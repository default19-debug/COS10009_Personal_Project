import pygame
from Setting import *

class Player:
    def __init__(self):
        self.x = WindowWidth / 2
        self.y =  WindowHeight / 2
        self.radius = 3
        self.RotateAngle = 0
        self.turnDireciton = 0
        self.walkDirection=0
        self.movespeed = 2.5
        self.Rotatespeed = 1
    def update(self):
        self.turnDireciton =0
        self.walkDirection =0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.turnDireciton = 0.1
        if keys[pygame.K_a]:
            self.turnDireciton = -0.1
        if keys[pygame.K_w]:
            self.walkDirection = 0.5
        if keys[pygame.K_s]:
            self.walkDirection = -0.5
        movestep = self.walkDirection * self.movespeed
        self.RotateAngle += self.turnDireciton * self.Rotatespeed
        self.x += math.cos(self.RotateAngle) * movestep
        self.y += math.sin(self.RotateAngle) * movestep


    def render(self,screen):
        pygame.draw.circle(screen,(255,0,0),(self.x, self.y),self.radius)
        pygame.draw.line(screen,(200,0,0),(self.x, self.y),(self.x + 40*math.cos(self.RotateAngle), self.y+ 40*math.sin(self.RotateAngle)))
