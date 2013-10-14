#! python3
import pygame
import sys
from pygame.locals import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCORES_HEIGHT = 100
FRAME_RATE = 60
WHITE = (255, 255, 255)

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
PLAYABLE_Y = (SCORES_HEIGHT, SCREEN_HEIGHT)


class Paddle:
    WIDTH = 10
    HEIGHT = 50
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
            new_y = y_h

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
    def setColor(self, color):
        self.color = color
    def setSpeed(self, x, y):
        self.speed = [x, y]
    def draw(self, surface):
        pygame.draw.circle(surface, self.color,
                           (self.x, self.y), self.radius)


def get_positions(y, pressed):      
    if pressed[K_UP] or pressed[K_w]:
        y -= 3
    if pressed[K_DOWN] or pressed[K_s]:
        y += 3

    if y + HEIGHT > PLAYABLE_Y[1]:
        y = PLAYABLE_Y[1] - HEIGHT
    elif y < PLAYABLE_Y[0]:
        y = PLAYABLE_Y[0]
    return y

def get_objects():
    '''Gives the 3 objects in the game'''
    player = Paddle(
        SCREEN_SIZE[0] // 20, SCREEN_SIZE[1] // 2,
        Paddle.WIDTH, Paddle.HEIGHT, WHITE)
    comp = Paddle(
        (18.7 * SCREEN_SIZE[0]) // 20, SCREEN_SIZE[1] // 2,
        Paddle.WIDTH, Paddle.HEIGHT, WHITE)
    ball = Ball(
        SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2,
        10, WHITE)

    return player, comp, ball

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock().tick

    player, comp, ball = get_objects()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pressed = pygame.key.get_pressed()
        p_y = get_positions(p_y, pressed)

        screen.fill((0, 0, 0))
        player.draw()
        comp.draw()
        ball.draw()
        
        pygame.display.flip()
        clock(FRAME_RATE)
    

if __name__ == "__main__":
    main()
