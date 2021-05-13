import pygame

from pathlib import Path

# Set this constant to make it simple to point to ressources folder
ASSETS = str(Path(__file__).resolve().parent) + "/ressources/"


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        # We call the init of parent class Sprite
        super().__init__()
        # We set a Game instance to check for collisions
        self.game = game
        # Assets will be 32x32 pixels, so we move 32 by 32.
        self.speed = 32
        # Load asset
        self.image = pygame.image.load(ASSETS + "player.png")
        # Rescale it 32 by 32
        self.image = pygame.transform.scale(self.image, (32, 32))
        # We create a rect in which we will draw its image
        # Will also be used to detect collisions
        self.rect = self.image.get_rect()
        # Default position is top left corner
        self.rect.x = 32
        self.rect.y = 32

    def moveUp(self):
        # Moves the rect, check for collision, cancel movement if collisition
        # with wall
        self.rect.y -= self.speed
        if self.game.check_collision(self, self.game.all_walls):
            self.rect.y += self.speed

    def moveDown(self):
        self.rect.y += self.speed
        if self.game.check_collision(self, self.game.all_walls):
            self.rect.y -= self.speed

    def moveLeft(self):
        self.rect.x -= self.speed
        if self.game.check_collision(self, self.game.all_walls):
            self.rect.x += self.speed

    def moveRight(self):
        self.rect.x += self.speed
        if self.game.check_collision(self, self.game.all_walls):
            self.rect.x -= self.speed

    def movements(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP]:  # Up arrow
            self.moveUp()
        if keys_pressed[pygame.K_DOWN]:  # Down arrow
            self.moveDown()
        if keys_pressed[pygame.K_LEFT]:  # Left arrow
            self.moveLeft()
        if keys_pressed[pygame.K_RIGHT]:  # Right arrow
            self.moveRight()
