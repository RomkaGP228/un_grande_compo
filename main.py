from data.params import *
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Un Grande Compo')
    window_size = window_width, window_height
    screen = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(black)
        pygame.display.flip()
    pygame.quit()



