
import pygame
import random
from color import RED


class Food:
    def __init__(self,cols, rows, cell_size):
        self.cols = cols
        self.rows = rows
        self.cell_size = cell_size
        self.position = (0,0)
        self.respawn()

    def respawn(self):
        x = random.randint(0,self.cols-1)
        y = random.randint(0,self.rows-1)
        self.position = (x,y)

    def get_position(self):
        return self.position

    def draw(self, surface):
        x,y = self.position
        rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(surface, RED, rect)