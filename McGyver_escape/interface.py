import pygame


def render_win_screen(clock, SCREEN, FPS):
    """Render win screen and exit message"""
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


def render_lose_screen(clock, SCREEN, FPS):
    """render lose screen, advice and exit message"""
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


def screen_update(clock, FPS, SCREEN, game):
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
        inventory_font = pygame.font.SysFont(None, 26)
        inventory_font_img = inventory_font.render(
            "Seringe crafted ! Put the guard to sleep and escape!",
            True, (255, 255, 255))
        SCREEN.blit(inventory_font_img, (10, 485))

    pygame.display.flip()
