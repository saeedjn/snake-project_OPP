import pygame
from color import BLACK, RED

from snake import Snake
from walls import Walls
from food import Food
from scoreManager import ScoreManager

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.paused = False
        self.cols, self.rows = 60, 60
        self.cell_size = 15
        self.screen = pygame.display.set_mode((self.cols * self.cell_size, self.rows * self.cell_size))
        pygame.display.set_caption("Snake Game version-OOP")
        self.clock = pygame.time.Clock()

        self.key_map = {
            pygame.K_UP : (0, -1),
            pygame.K_DOWN: (0, 1),
            pygame.K_LEFT: (-1, 0),
            pygame.K_RIGHT: (1, 0),

            pygame.K_w: (0, -1),
            pygame.K_s: (0, 1),
            pygame.K_a: (-1, 0),
            pygame.K_d: (1, 0)
        }

        self.snake = Snake(start_pos=(10,10))

        self.walls = Walls(self.cols,self.rows,self.cell_size,True,5)

        self.food = Food(self.cols, self.rows,self.cell_size,self.snake.body,self.walls.get_walls())

        self.score = ScoreManager()


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)

    def handle_events(self):
        for event in pygame.event.get():
            pygame.time.wait(1)
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN :
                if event.key in self.key_map :
                    new_dir = self.key_map[event.key]
                    self.snake.set_direction(new_dir)
                if event.key == pygame.K_SPACE :
                    self.paused = not self.paused

    def update(self):
        if self.paused:
            return

        self.snake.move()
        if self.snake.check_collision(self.cols,self.rows,self.walls.get_walls(),tunnel=True):
            self.running = False


        if self.snake.get_head() == self.food.position:
            self.score.add_score()
            self.snake.grow()
            self.food.snake_body = self.snake.body
            self.food.generate_new_food()


    def draw(self):
        font = pygame.font.SysFont("Arial", 20)
        if self.paused:
            text = font.render("PAUSE", True, RED)
            rect = text.get_rect()
            rect.center = self.screen.get_width()//2, self.screen.get_height()//2
            self.screen.blit(text, rect)

        self.screen.fill(BLACK)
        self.walls.draw(self.screen)
        self.snake.draw(self.screen,self.cell_size)
        self.score.draw(self.screen,font)
        self.food.draw(self.screen)

        pygame.display.update()