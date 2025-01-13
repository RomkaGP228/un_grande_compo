from data.player import *
from data.ray_casting import *
from data.draw import Draw

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Un Grande Compo')
    window_size = window_width, window_height
    screen = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()
    player = Player()
    draw_example = Draw(screen, world_map)
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
        else:
            pygame.mouse.set_visible(False)
        screen.fill(black)
        draw_example.draw_world(player.pos, player.angle)
        draw_example.draw_fps(clock)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
