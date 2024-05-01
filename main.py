import pygame
from pygame.locals import *
from random import randint
from math import sqrt

#window size, can be changed depending on needs
window_size = 1000

#window size is used both as width and height, as we need a square window in order for the simulation to be accurate
screen = pygame.display.set_mode((window_size,window_size))

#define variables to store how many points are in the circle and how many there are in total
points_in_circle = 0
total_points = 0

#fill the background once
screen.fill("white")

#define a variable to leave the loop
done = False

while not done:
    #get events
    for event in pygame.event.get():
        #if there's a quit event, set done as false
        if event.type == QUIT:
            done = True

    #generate a random x and y in the window
    rand_x = randint(0,window_size)
    rand_y = randint(0,window_size)

    #check if the distance to the origin is bigger than the window-size ie. is outside the circle
    if (sqrt(rand_x**2+rand_y**2) <= window_size):
        #if it's in the cirlce draw a green pixel and add 1 to the points in the circle
        screen.set_at((rand_x,rand_y), "green")
        points_in_circle += 1

    else:
        #else draw a red pixel
        screen.set_at((rand_x,rand_y), "red")
    #add 1 to the total points
    total_points += 1

    #set the estimated value of pi as the caption of the window
    pygame.display.set_caption(f"Pi = {4* points_in_circle / total_points}")
    #update the screen
    pygame.display.update()

#before exiting the program, make sure pygame is properly closed
pygame.quit()

    

