from data.map import *
from data.player import *
from math import sin, cos
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
    print(world_map)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.move()
        screen.fill(black)
        draw_example.draw_world(player.pos, player.angle)
        draw_example.draw_fps(clock)
        # pygame.draw.circle(screen, white, player.pos, 20)
        # pygame.draw.line(screen, white, player.pos, (player.x + cos(player.angle) * 1000,player.y + sin(player.angle) * 1000))
        # for x, y in world_map:
        #     pygame.draw.rect(screen, white, (x, y, wall_size, wall_size), 5)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()



