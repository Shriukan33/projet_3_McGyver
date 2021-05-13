from pathlib import Path

import pygame

from game import Game

# Set this constant to make it simple to point to ressources folder
ASSETS = str(Path(__file__).resolve().parent) + "/ressources/"

# Initialize the pygame modules
pygame.init()

# General display settings
pygame.display.set_caption("McGyver escape")
SCREEN = pygame.display.set_mode((32*15, 32*15))
# Framerate control, no need to have a high count as the movement isn't fluid
clock = pygame.time.Clock()
FPS = 24
# Initialize the game
game = Game()

running = True

# Main game loop
while running:
    clock.tick(FPS)
    # Filling the bacground in black, it's dungeon-like
    SCREEN.fill((0, 0, 0))
    # Draws player
    SCREEN.blit(game.player.image, game.player.rect)
    # Draws walls of labyrinth
    game.all_walls.draw(SCREEN)
    game.all_items.draw(SCREEN)

    pygame.display.flip()

    # This loops through all events of the game
    for event in pygame.event.get():

        # Check if we are quitting the game
        if event.type == pygame.QUIT:
            running = False
            pygame.QUIT

        # Placed here, holding the key will not produce
        # several movements.
        game.player.movements()
