import pygame

from color import GREEN


class Snake:
    def __init__(self,start_pos, initial_length=3, initial_dir=(1,0)):
        x,y = start_pos
        self.body = [(x - i ,y) for i in range(initial_length)]
        self.direction = initial_dir
        self.grow_pending = 0

    def get_head(self):
        return self.body[0]

    def set_direction(self,new_dir):
        opposite = (-self.direction[0],-self.direction[1])
        if new_dir != opposite:
            self.direction = new_dir

    def move(self):
        head_x, head_y = self.get_head()
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        self.body.insert(0, new_head)

        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self, amount=1):
        self.grow_pending += amount

    def check_self_collision(self):
        head = self.get_head()
        return head in self.body[1:]

    def check_collision(self,cols,rows,walls=None,tunnel=False):
        head = self.get_head()
        x,y = head

        if self.check_self_collision():
            return True

        if not tunnel:
            if x < 0 or x >= cols or y < 0 or y >= rows:
                return True
        else:
            x = x % cols
            y = y % rows
            self.body[0] = (x,y)

        if walls:
            all_cells = []
            if len(walls) > 0 and isinstance(walls[0], (list, tuple)):
                for wall in walls:
                    all_cells.append(wall)
            else:
                all_cells = list(walls)

            if self.get_head() in all_cells:
                return True

        return False

    def reset(self, start_pos, initial_length=3, initial_dir=(1,0)):
        x,y = start_pos
        self.body = [(x - i,y) for i in range(initial_length)]
        self.direction = initial_dir
        self.grow_pending = 0


    def draw(self, surface, cell_size, color=GREEN, head_color=None):

        for i, (x,y) in enumerate(self.body):
            rect = pygame.Rect(x*cell_size, y*cell_size, cell_size,cell_size)
            if i == 0 and head_color:
                pygame.draw.rect(surface, head_color, rect)
            else:
                pygame.draw.rect(surface, color, rect)

