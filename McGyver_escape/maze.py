import pygame
from pathlib import Path

class Maze:
    
    def __init__(self):
        self.x = 15
        self.y = 15
        self.maze = [
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,2,0,0,0,1,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,1,0,0,0,0,0,1,1,0,1,
            1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,
            1,0,1,0,0,1,0,0,1,1,0,0,1,0,1,
            1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,
            1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,
            1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,
            1,0,1,1,1,1,1,1,1,0,0,1,1,0,1,
            1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,
            1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,
            1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,
            1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,
            1,0,0,0,0,1,0,0,1,0,0,0,1,3,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,4,1
        ]
        # 1 = Walls, 2 = Start, 3 =  Guard, 4 = Exit

    def draw(self, WIN, image):
        column = 0
        row = 0

        for tile in range(self.x * self.y):
            if self.maze[row + column * self.y] == 1: # Walls
                WIN.blit(image, (row * 32, column * 32)) # Will use 32px assets

            column += 1 # Right tile next
            if column > self.x-1: # If we are at the border, go back to left and next line
                column = 0
                row += 1

class Player:

    x, y = 32, 32
    speed = 32

    # TODO: Add collision 
    def moveUp(self):
        self.y -= self.speed
    
    def moveDown(self):
        self.y += self.speed
    
    def moveLeft(self):
        self.x -= self.speed
    
    def moveRight(self):
        self.x += self.speed

    def detect_collision(self):
        pass

class App:

    # 32 * 15 = 480
    width = 480
    height = 480

    def __init__(self):
        self._running = True

        # Window parameters
        self.WIN = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("McGyver mon héros")

        # Wall assets
        self.wall_image = pygame.image.load(Path(__file__).parent / "ressources" / "wall.png")
        self.wall = pygame.transform.scale(self.wall_image, (32, 32)) # 32 by 32 blocs
        
        # Player assets
        self.player = Player()
        self.player_image = pygame.image.load(Path(__file__).parent / "ressources" / "player.png")
        self.player_image = pygame.transform.scale(self.player_image, (32, 32))

        # Maze
        self.maze = Maze()

    def render(self):
        self.WIN.fill((0,0,0))  # Black background
        self.WIN.blit(self.player_image, (self.player.x, self.player.y)) # Draw player
        self.maze.draw(self.WIN, self.wall) # Draw maze
        pygame.display.flip() # Update the whole screen 

    def movements(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP]: # Up arrow
            self.player.moveUp()
        if keys_pressed[pygame.K_DOWN]: # Down arrow
            self.player.moveDown()
        if keys_pressed[pygame.K_LEFT]: # Left arrow
            self.player.moveLeft()
        if keys_pressed[pygame.K_RIGHT]: # Right arrow
            self.player.moveRight()


    def play(self):

        # Framerate parameters
        clock = pygame.time.Clock()
        FPS = 24

        while self._running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    pygame.quit()

                self.movements()

                self.render()   

if __name__ == '__main__':
    app = App()
    app.play()