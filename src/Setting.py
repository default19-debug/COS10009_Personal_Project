import math
TileSize = 35
Rows=20
Col=20
WindowWidth = Col*TileSize
WindowHeight = Rows*TileSize
FOV = 60 * (math.pi/180) #60 deg in Rad
RES =  1 #Resolution
NRays = WindowWidth // RES #formula for how many rays to be cast
Total_debug_hours = "7 hours 20 minutes"