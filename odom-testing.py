# README:
# Quick testing of odometry on a simulated bot + visualization
# Currently implemented: distance formula between 2 coordinates

import matplotlib.pyplot as plt
import numpy as np
import pygame
import math

pygame.init()
win = pygame.display.set_mode((900, 900))
pygame.display.set_caption("odom + movement testing")

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

x = 0
y = 0
width = 40
height = 60
vel = 1

font = pygame.font.Font('Raleway-Bold.ttf', 32)

dist = 0


run = True


def calc_dist(origin_x, origin_y, curr_x, curr_y):
    d = math.sqrt((curr_x - origin_x)**2) + math.sqrt((curr_y - origin_y)**2)
    return d

while run:
    text = font.render(f"Dist: {calc_dist(0, 0, x, y)}", True, green, blue)
    textRect = text.get_rect()
    textRect.center = (700, 700)
    
    
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        x -= vel
    if keys[pygame.K_d]:
        x += vel
    if keys[pygame.K_w]:
        y -= vel
    if keys[pygame.K_s]:
        y += vel
    
    
    
    win.fill(black)
    win.blit(text, textRect)
    pygame.draw.rect(win, red, (x, y, width, height))
    pygame.draw.line(win, green, (0, 0), (x, y))
    pygame.display.update()
pygame.quit