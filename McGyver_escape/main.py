import pygame

from game import Game


def main():

    # Initialize the pygame modules
    pygame.init()

    # General display settings
    pygame.display.set_caption("McGyver escape")
    SCREEN = pygame.display.set_mode((32*15, 32*16))
    # Framerate control
    clock = pygame.time.Clock()
    FPS = 24

    running = True

    # Main game loop
    while running:

        # Initialize the game
        game = Game()

        while game.main_game:
            clock.tick(FPS)
            # Filling the bacground in black, it's dungeon-like
            SCREEN.fill((0, 0, 0))
            # Draws all assets
            game.all_walls.draw(SCREEN)
            game.all_items.draw(SCREEN)
            game.all_guards.draw(SCREEN)
            game.all_exits.draw(SCREEN)
            game.all_players.draw(SCREEN)

            # Inventory display, clears the objective
            if game.inventory != 3:
                inventory_font = pygame.font.SysFont(None, 26)
                inventory_font_img = inventory_font.render(
                    "Gather all 3 items to craft a seringe ! ({}/3)".format(
                        game.inventory),
                    True, (255, 255, 255))
                SCREEN.blit(inventory_font_img, (10, 485))
            elif game.inventory == 3:
                inventory_font_img = inventory_font.render(
                    "Seringe crafted ! Put the guard to sleep and escape!",
                    True, (255, 255, 255))
                SCREEN.blit(inventory_font_img, (10, 485))

            # Check if Mc giver is picking up an object
            for item in game.all_items:
                item.check_pick_up()

            # Check If McGyver is engaging a fight with the guard
            for guard in game.all_guards:
                guard.check_fight()

            # Check if Mc Gyver is out !
            for exit in game.all_exits:
                exit.check_exit()

            pygame.display.flip()

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
                    if event.key == pygame.K_UP:
                        game.player.moveUp()
                    if event.key == pygame.K_DOWN:
                        game.player.moveDown()
                    if event.key == pygame.K_RIGHT:
                        game.player.moveRight()
                    if event.key == pygame.K_LEFT:
                        game.player.moveLeft()

        # Lose screen enabled when you encounter a guard and don't have all
        # items
        while game.lose_screen:

            clock.tick(FPS)
            SCREEN.fill((0, 0, 0))

            MESSAGE_COLOR = (255, 255, 255)

            lose_text = pygame.font.SysFont(None, 36, True)
            lose_text_img = lose_text.render("You lost !", True, MESSAGE_COLOR)
            text_rect = lose_text_img.get_rect(center=(240, 200))
            SCREEN.blit(lose_text_img, text_rect)

            instruction_text = pygame.font.SysFont(None, 30)
            instruction_text_img = instruction_text.render(
                "Get all 3 items before fighting the guard !",
                True, MESSAGE_COLOR)
            text_rect = instruction_text_img.get_rect(center=(240, 240))
            SCREEN.blit(instruction_text_img, text_rect)

            lose_subtext = pygame.font.SysFont(None, 24)
            lose_subtext_img = lose_subtext.render(
                "Press any key to exit the game.", True, MESSAGE_COLOR)
            text_rect = lose_subtext_img.get_rect(center=(240, 280))
            SCREEN.blit(lose_subtext_img, text_rect)
            pygame.display.flip()

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

            clock.tick(FPS)
            SCREEN.fill((0, 0, 0))

            MESSAGE_COLOR = (255, 255, 255)

            win_text = pygame.font.SysFont(None, 36, True)
            win_text_img = win_text.render("YOU WON !", True, MESSAGE_COLOR)
            text_rect = win_text_img.get_rect(center=(240, 200))
            SCREEN.blit(win_text_img, text_rect)

            win_subtext = pygame.font.SysFont(None, 24)
            win_subtext_img = win_subtext.render(
                "Press any key to exit the game.", True, MESSAGE_COLOR)
            text_rect = win_subtext_img.get_rect(center=(240, 240))
            SCREEN.blit(win_subtext_img, text_rect)

            # Updates the screen
            pygame.display.flip()

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
