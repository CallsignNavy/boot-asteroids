import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # setting framerate to 60 FPS
        dt = clock.tick(60) / 1000

        screen.fill("black")

        player.update(dt)

        player.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()
