
import pygame
import random
from color import RED


class Food:
    def __init__(self,cols, rows, cell_size, snake_body=None, walls=None):
        self.cols = cols
        self.rows = rows
        self.cell_size = cell_size
        self.position = (0,0)
        self.snake_body = snake_body if snake_body else []
        self.walls = walls if walls else []
        self.generate_new_food()

    def generate_new_food(self):
        while True:
            x = random.randint(0,self.cols-1)
            y = random.randint(0,self.rows-1)
            pos = (x,y)
            if pos not in self.snake_body and pos not in self.walls:
                self.position = pos
                break

    def get_position(self):
        return self.position

    def draw(self, surface):
        x,y = self.position
        rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(surface, RED, rect)