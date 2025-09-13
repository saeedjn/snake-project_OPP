import pygame
from color import BLACK

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((600,400))
        pygame.display.set_caption("Snake Game version-OOP")
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)
        pygame.display.update()