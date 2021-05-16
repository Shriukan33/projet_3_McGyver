from pathlib import Path

import pygame

# Set this constant to make it simple to point to ressources folder
ASSETS = str(Path(__file__).resolve().parent) + "/ressources/"


class Guard(pygame.sprite.Sprite):
    """Guard handles the collision and appearance of guards in the maze"""

    def __init__(self, game, x_pos, y_pos):
        super().__init__()
        self.game = game
        self.image = pygame.image.load(ASSETS + "guard.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def check_fight(self):
        """Checks if player collides with guard and handle consequences.

        If the player has 3 items, guard dies.
        Otherwise, player dies and lose screen is enabled.
        """

        if self.game.check_collision(self, self.game.all_players):
            if self.game.inventory == 3:
                self.kill()
            else:
                self.game.main_game = False
                self.game.lose_screen = True
