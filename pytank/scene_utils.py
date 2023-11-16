import math

def get_xy_proj(dist, heading):
    heading_r=math.radians(heading)
    dx=math.sin(heading_r)*dist
    dy=-math.cos(heading_r)*dist
    return (dx, dy)
