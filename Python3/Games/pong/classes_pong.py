import pygame

class Paddle:
    WIDTH = 10
    HEIGHT = 50
    SPEED = 3
    #Class Initialization
    def __init__(self, x, y, width, height, color):
        self.width = 0
        self.height = 0
        self.setPosition(x, y)
        self.setDimension(width, height)
        self.setColor(color)
        self.setSpeed(0, 0)
    #Main Functions
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        self.setRect()
    def setDimension(self, width, height):
        self.width = width
        self.height = height
        self.setRect()
    def setColor(self, color):
        self.color = color
    def setSpeed(self, x, y):
        self.speed = [x, y]
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

        self.setPosition(new_x, new_y)
        
    #Auxillary Functions
    def setRect(self):
        self.rect = pygame.Rect(
            self.x, self.y, self.width, self.height)

class Ball:
    #Class Initialization
    def __init__(self, x, y, radius, color):
        self.setPosition(x, y)
        self.setRadius(radius)
        self.setColor(color)
        self.setSpeed(0, 0)
    #Main Functions
    def setPosition(self, x, y):
        self.x = x
        self.y = y
    def setRadius(self, radius):
        self.radius = radius
    def setColor(
        self, color):
        self.color = color
    def setSpeed(self, x, y):
        self.speed = [x, y]
    def draw(self, surface):
        pygame.draw.circle(surface, self.color,
                           (self.x, self.y), self.radius)

class ScoreArea:
    LINE_WIDTH = 15
    COLOR = (128, 128, 128)
    #Class Initialization
    def __init__(self, scores_height, screen_width):
        self.rect = pygame.Rect(
            0, scores_height - ScoreArea.LINE_WIDTH, screen_width,
            ScoreArea.LINE_WIDTH)
    #Main Functions
    def draw(self, surface):
        pygame.draw.rect(surface, self.COLOR, self.rect)
