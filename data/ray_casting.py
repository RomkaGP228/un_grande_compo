from math import sin, cos
from data.params import *
from data.map import wrld_width, wrld_height


def mapping(x, y):
    # для нахождения текущей позиции игрока в квадрате
    return (x // wall_size) * wall_size, (y // wall_size) * wall_size


def ray_casting(player, world_map, textures):
    # для отрисовки мира вокруг (та самая технология ray casting)
    walls = []
    angle = player.angle - view_field_half
    x0, y0 = player.pos
    xam, yam = mapping(x0, y0)
    texture_vert, texture_hor = 1, 1
    for ray in range(nums_rays):
        sin_a = sin(angle)
        cos_a = cos(angle)

        # verticals
        if cos_a >= 0:
            x = xam + wall_size
            dx = 1
        else:
            x = xam
            dx = -1
        for _ in range(0, wrld_width, wall_size):
            dpth_vert = (x - x0) / cos_a
            y_vert = y0 + dpth_vert * sin_a
            tile_vert = mapping(x + dx, y_vert)
            if tile_vert in world_map:
                texture_vert = world_map[tile_vert]
                break
            x += dx * wall_size

        # horizontals
        if sin_a >= 0:
            y = yam + wall_size
            dy = 1
        else:
            y = yam
            dy = -1
        for _ in range(0, wrld_height, wall_size):
            dpth_hor = (y - y0) / sin_a
            x_hor = x0 + dpth_hor * cos_a
            tile_hor = mapping(x_hor, y + dy)
            if tile_hor in world_map:
                texture_hor = world_map[tile_hor]
                break
            y += dy * wall_size

        depth, offset, texture = (dpth_vert, y_vert, texture_vert) if dpth_vert < dpth_hor else (
            dpth_hor, x_hor, texture_hor)
        offset = int(offset) % wall_size
        depth *= cos(player.angle - angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(coeff / depth), 5 * window_height)
        wall_column = textures[texture].subsurface(offset * texture_scale, 0, texture_scale, texture_height)
        wall_column = pygame.transform.scale(wall_column, (scale, proj_height))
        wall_pos = (ray * scale, window_height // 2 - proj_height // 2)
        walls.append((depth, wall_column, wall_pos))
        angle += d_rays
    return walls
