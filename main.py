from data.player import *
from data.ray_casting import *
from data.draw import Draw
from data.map import world_map_maker, first_map, second_map
from data.sprites import *
from data.saver import *

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Un Grande Compo')
    window_size = window_width, window_height
    screen = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()
    first_time()

    player = Player()
    sprites = SpriteClass()
    main_map = second_map
    world_map = world_map_maker(main_map)
    draw_example = Draw(screen, world_map, player)
    running = True
    draw_example.menu()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.movement()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.mouse.set_visible(True)
            draw_example.pause()
        if (790 <= player.pos[0] <= 830) and (500 <= player.pos[1] <= 540) and main_map == first_map:
            main_map = second_map
            world_map = world_map_maker(main_map)

        else:
            pygame.mouse.set_visible(False)
        screen.fill(black)
        walls = ray_casting(player, world_map, draw_example.textures)
        draw_example.draw_world(walls + [obj.object_locate(player, walls) for obj in sprites.obj_list])
        draw_example.draw_fps(clock)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
