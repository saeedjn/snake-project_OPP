
import pygame
import random
from color import ORANGE

class Walls:
    def __init__(self, cols, rows,cell_size,random_mode=False, count=5):
        self.cols = cols
        self.rows = rows
        self.cell_size = cell_size
        self.random_mode = random_mode
        self.count = count
        self.walls = []
        self.generate_walls()

    def generate_walls(self):
        self.walls.clear()
        if self.random_mode:
            for _ in range(self.count):
                x = random.randint(0, self.cols - 1)
                y = random.randint(0, self.rows - 1)
                pos = (x,y)
                if pos not in self.walls:
                    self.walls.append(pos)

        else:
            for x in range(self.cols):
                self.walls.append((x,0))
                self.walls.append((x,self.rows - 1))

            for y in range(self.rows):
                self.walls.append((0,y))
                self.walls.append((self.cols - 1,y))

    def get_walls(self):
        return self.walls

    def draw(self, surface):
        for (x,y) in self.walls:
            rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(surface, ORANGE, rect)
