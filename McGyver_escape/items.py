import pygame
from pathlib import Path

# Set this constant to make it simple to point to ressources folder
ASSETS = str(Path(__file__).resolve().parent) + "/ressources/"


class Items(pygame.sprite.Sprite):

    def __init__(self, game, asset_name, x_pos, y_pos):
        super().__init__()
        self.game = game
        self.image = pygame.image.load(ASSETS + asset_name)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def check_pick_up(self):
        if self.game.check_collision(self, self.game.all_players):
            self.game.inventory += 1
            print("Inventory : ", self.game.inventory)
            self.kill()
