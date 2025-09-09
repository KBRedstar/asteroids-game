import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    game_clock = pygame.time.Clock()
    game_dt = 0
    game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        game_screen.fill("black")
        updatable.update(game_dt)
        for p in drawable:
            p.draw(game_screen)
        pygame.display.flip()

        game_dt = game_clock.tick(60) / 1000

    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
