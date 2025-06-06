import pygame
import sys
from utils.config import Config


def main():
    pygame.init()
    
    screen = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
    pygame.display.set_caption(Config.WINDOW_TITLE)
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(Config.BACKGROUND_COLOR)
        
        pygame.display.flip()
        clock.tick(Config.FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()