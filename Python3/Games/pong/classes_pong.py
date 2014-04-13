import pygame


class Shape:
    def __init__(self):
        self.color = (0, 0, 0)
        self.speed = [0, 0]
        self.x = 0
        self.y = 0

    def set_color(self, color):
        self.color = color

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_speed(self, x, y):
        self.speed = [x, y]


class Paddle(Shape):
    WIDTH = 10
    HEIGHT = 50
    SPEED = 3

    def __init__(self, x, y, color, width=WIDTH, height=HEIGHT):
        super().__init__()
        self.width = 0
        self.height = 0
        self.rect = None
        self.set_position(x, y)
        self.set_color(color)
        self.set_dimension(width, height)

    #Main Functions
    def set_position(self, x, y):
        super().set_position(x, y)
        self.set_rect()

    def set_dimension(self, width, height):
        self.width = width
        self.height = height
        self.set_rect()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, x_l, x_h, y_l, y_h):
        new_x = self.x + self.speed[0]
        new_y = self.y + self.speed[1]

        if new_x < x_l:
            new_x = x_l
        elif new_x + self.width > x_h:
            new_x = x_h

        if new_y < y_l:
            new_y = y_l
        elif new_y + self.height > y_h:
            new_y = y_h - self.height

        self.set_position(new_x, new_y)

    #Auxillary Functions
    def set_rect(self):
        self.rect = pygame.Rect(
            self.x, self.y, self.width, self.height)


class Ball(Shape):
    def __init__(self, x, y, radius, color):
        super().__init__()
        self.radius = 0
        self.set_position(x, y)
        self.set_radius(radius)
        self.set_color(color)

    def set_radius(self, radius):
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, self.color,
                           (self.x, self.y), self.radius)


class ScoreArea:
    LINE_WIDTH = 15
    COLOR = (128, 128, 128)

    def __init__(self, scores_height, screen_width):
        self.rect = pygame.Rect(
            0, scores_height - ScoreArea.LINE_WIDTH, screen_width,
            ScoreArea.LINE_WIDTH)

    #Main Functions
    def draw(self, surface):
        pygame.draw.rect(surface, self.COLOR, self.rect)
