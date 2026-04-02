import math
import pygame
from Setting import *
def normalizeAngle(angle):
    angle = angle % (2 * math.pi)
    if (angle < 0):
        angle = (2 * math.pi) + angle
    return angle

def distancebetween(x1, y1 ,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1)  +  (y2-y1)*(y2-y1))

class Ray:

    def __init__(self,angle,player,Map):
        self.Rayangle = normalizeAngle(angle)
        self.player = player
        self.is_facing_down = self.Rayangle >0 and self.Rayangle < math.pi
        self.is_facing_up = not self.is_facing_down
        self.is_facing_right = self.Rayangle < 0.5 * math.pi or self.Rayangle > 1.5 * math.pi
        self.is_facing_left = not self.is_facing_right
        self.Map = Map
        self.wall_hit_x = 0
        self.wall_hit_y= 0
        self.distance = 0
        self.color = 255
        self.wall_type = 1

    def cast(self,screen):
        Found_horizontal_wall = False
        horizontal_hit_x =0
        horizontal_hit_y =0
        first_intersect_x = None
        first_intersect_y = None
        hort_wall_type = 1
        vert_wall_type = 1

        if self.is_facing_up:
            first_intersect_y = ((self.player.y)// TileSize ) *TileSize -0.001
        elif self.is_facing_down:
            first_intersect_y = ((self.player.y)// TileSize ) *TileSize + TileSize

        first_intersect_x = self.player.x + (first_intersect_y - self.player.y) / math.tan(self.Rayangle)
        next_horizontal_x = first_intersect_x
        next_horizontal_y = first_intersect_y
        xa =0
        xy =0
        if self.is_facing_up:
            ya = -TileSize
        elif self.is_facing_down:
            ya = TileSize
        xa = ya/math.tan(self.Rayangle)

        while (next_horizontal_x <= WindowWidth and next_horizontal_x >= 0 and next_horizontal_y <= WindowHeight and next_horizontal_y >= 0):
            if self.Map.Has_wall_at(next_horizontal_x , next_horizontal_y):
                Found_horizontal_wall = True
                horizontal_hit_x = next_horizontal_x
                horizontal_hit_y = next_horizontal_y
                self.wall_hit_x = horizontal_hit_x
                self.wall_hit_y = horizontal_hit_y
                hort_wall_type = self.Map.Get_wall_type(next_horizontal_x, next_horizontal_y)
                break

            else:
                next_horizontal_x += xa
                next_horizontal_y += ya
                self.wall_hit_x = self.player.x + math.cos(self.Rayangle) * 1000
                self.wall_hit_y = self.player.y + math.sin(self.Rayangle) * 1000



        Found_vert_wall= False
        vert_hit_x = 0
        vert_hit_y =0
        if self.is_facing_right:
            first_intersect_x = ((self.player.x // TileSize) * TileSize) +TileSize
        elif self.is_facing_left:
            first_intersect_x = (((self.player.x) // TileSize)*TileSize -0.001)

        first_intersect_y = self.player.y + (first_intersect_x -self.player.x) * math.tan(self.Rayangle)

        next_vert_x = first_intersect_x
        next_vert_y = first_intersect_y
        if self.is_facing_right:
            xa = TileSize
        elif self.is_facing_left:
            xa = -TileSize

        ya = xa * math.tan(self.Rayangle)
        while (next_vert_x <= WindowWidth and next_vert_x >= 0 and next_vert_y <= WindowHeight and next_vert_y >= 0):
            if self.Map.Has_wall_at(next_vert_x , next_vert_y):
                Found_vert_wall = True
                vert_hit_x = next_vert_x
                vert_hit_y = next_vert_y
                vert_wall_type = self.Map.Get_wall_type(next_vert_x, next_vert_y)
                break
            else:
                next_vert_x += xa
                next_vert_y += ya

            #Distance calculation:

        hort_dist = 0
        vert_dist = 0
        if Found_horizontal_wall:
            hort_dist = distancebetween(self.player.x , self.player.y
            , horizontal_hit_x , horizontal_hit_y)
        else:
            hort_dist = 9999

        if Found_vert_wall:
            vert_dist = distancebetween(self.player.x , self.player.y
                                        , vert_hit_x , vert_hit_y)
        else:
            vert_dist = 9999

        if hort_dist < vert_dist:
            self.wall_hit_x = horizontal_hit_x
            self.wall_hit_y = horizontal_hit_y
            self.distance = hort_dist
            self.color = 160
            self.wall_type = hort_wall_type
        else:
            self.wall_hit_x = vert_hit_x
            self.wall_hit_y = vert_hit_y
            self.distance = vert_dist
            self.color = 255
            self.wall_type = vert_wall_type


        self.distance *= math.cos(self.player.RotateAngle - self.Rayangle)
        self.color *= (50/self.distance) #60 is light level, reduce to make it darker
        round(self.color) #keep it an int
        if self.color >255:
            self.color = 255
        elif self.color <0:
            self.color = 0
    def render(self, screen):
        pygame.draw.line(screen,(255,0,50) , (self.player.x ,self.player.y),
                         (self.wall_hit_x,self.wall_hit_y))


