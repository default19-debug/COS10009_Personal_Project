import pygame
import math
from Setting import *

class Player:
    def __init__(self):
        self.x = WindowWidth / 2
        self.y = WindowHeight / 2
        self.radius = 3

        self.RotateAngle = 0
        self.turnDireciton = 0
        self.walkDirection = 0

        self.movespeed = 1
        self.Rotatespeed = 1

        self.mouse_sens = 0.001
        pygame.mouse.get_rel()

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
        self.x += dx
        self.y += dy

    def render(self, screen):
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), self.radius)
        pygame.draw.line(
            screen,
            (200,0,0),
            (self.x, self.y),
            (self.x + 40 * math.cos(self.RotateAngle),
             self.y + 40 * math.sin(self.RotateAngle))
        )
