from data.params import *

map = ['111111111111',
       '100000000001',
       '100110000001',
       '100010011001',
       '100000011001',
       '100000000001',
       '111111111111',]

world_map = set()
for k1, i in enumerate(map):
    for k2, j in enumerate(i):
        if j == '1':
            world_map.add((k2 * wall_size, k1 * wall_size))
