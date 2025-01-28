from data.params import *
import json
import pathlib



with open(pathlib.PurePath("levels1/levels.json"), mode='r') as json_map_file:
    maps = json.load(json_map_file)
    first_map = maps["FirstMap"]
    second_map = maps["SecondMap"]

wrld_width = len(first_map[0]) * wall_size
wrld_height = len(second_map) * wall_size
collision_walls = []


def world_map_maker(new_map):
    world_map = {}
    for k1, i in enumerate(new_map):
        for k2, j in enumerate(i):
            if j:
                collision_walls.append(pygame.Rect(k2 * wall_size, k1 * wall_size, wall_size, wall_size))
                if j == 1:
                    world_map[(k2 * wall_size, k1 * wall_size)] = 1
                elif j == 2:
                    world_map[(k2 * wall_size, k1 * wall_size)] = 2
                elif j == 3:
                    world_map[(k2 * wall_size, k1 * wall_size)] = 3
                elif j == 4:
                    world_map[(k2 * wall_size, k1 * wall_size)] = 4
                elif j == 5:
                    world_map[(k2 * wall_size, k1 * wall_size)] = 5
    print(collision_walls)
    return world_map