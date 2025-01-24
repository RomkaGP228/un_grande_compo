from data.params import *
import json
import pathlib



with open(pathlib.PurePath("levels1/levels.json"), mode='r') as json_map_file:
    maps = json.load(json_map_file)
    first_map = maps["FirstMap"]
    second_map = maps["SecondMap"]

wrld_width = len(first_map[0]) * wall_size
wrld_height = len(second_map) * wall_size

def world_map_maker(new_map):
    world_map = set()

    for k1, i in enumerate(new_map):
        for k2, j in enumerate(i):
            if j == 1:
                world_map.add((k2 * wall_size, k1 * wall_size))
    return world_map