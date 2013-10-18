#! python3
from classes_pong import Paddle, Ball, Boundary
import pygame
import sys
from pygame.locals import *


#Constants for Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCORES_HEIGHT = 100
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
PLAY_AREA = (0, SCREEN_WIDTH, SCORES_HEIGHT, SCREEN_HEIGHT)

#Other Game constants
FRAME_RATE = 60
WHITE = (255, 255, 255)

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
    boundary = Boundary(SCORES_HEIGHT, SCREEN_WIDTH)
    
    return player, comp, ball, boundary


def movement(cur_pad):
    cur_pad.setSpeed(0, 0)
    pressed = pygame.key.get_pressed()
    if pressed[K_UP] or pressed[K_w]:
        cur_pad.setSpeed(0, -Paddle.SPEED)
    if pressed[K_DOWN] or pressed[K_s]:
        cur_pad.setSpeed(0, Paddle.SPEED)
    cur_pad.move(*PLAY_AREA)
    

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock().tick

    player, comp, ball, boundary = get_objects()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


        screen.fill((0, 0, 0))
        boundary.draw(screen)
        movement(player)
        player.draw(screen)
        comp.draw(screen)
        ball.draw(screen)
        
        pygame.display.flip()
        clock(FRAME_RATE)
    

if __name__ == "__main__":
    main()
