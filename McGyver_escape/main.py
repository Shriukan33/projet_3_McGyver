import pygame

from game import Game
import interface
from player import Player


def main():

    # Initialize the pygame modules
    pygame.init()

    # General display settings
    pygame.display.set_caption("McGyver escape")
    SCREEN = pygame.display.set_mode((32*15, 32*16))
    # Framerate control
    clock = pygame.time.Clock()
    FPS = 60

    running = True

    # Main game loop
    while running:

        # Initialize the game
        game = Game()

        while game.main_game:
            clock.tick(FPS)

            Player.interaction_check(game)
            interface.screen_update(clock, FPS, SCREEN, game)

            # This loops through all events of the game
            for event in pygame.event.get():

                # Check if we are quitting the game
                if event.type == pygame.QUIT:
                    running = False
                    game.main_game = False
                    pygame.quit()

                # Placed here, holding the key will not produce
                # several movements.
                if event.type == pygame.KEYDOWN:
                    Player.player_movements(event, game)

        # Lose screen enabled when you encounter a guard and don't have all
        # items
        while game.lose_screen:

            interface.render_lose_screen(clock, SCREEN, FPS)

            for event in pygame.event.get():

                # Check if we are quitting the game
                if event.type == pygame.QUIT:
                    running = False
                    game.lose_screen = False

                if event.type == pygame.KEYDOWN:
                    running = False
                    game.lose_screen = False

        # Win screen enabled when getting to the exit
        while game.win_screen:

            interface.render_win_screen(clock, SCREEN, FPS)

            for event in pygame.event.get():

                # Check if we are quitting the game
                if event.type == pygame.QUIT:
                    running = False
                    game.win_screen = False

                if event.type == pygame.KEYDOWN:
                    running = False
                    game.win_screen = False

        # Exit the game
        running = False


if __name__ == '__main__':
    main()
