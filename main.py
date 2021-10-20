import pygame
from pygame.locals import *

pygame.init()

# Set screen width to 1000
screen_width = 1000

# set screen height to 1000
screen_height = 1000

# Adds a screen
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('A Very Simple Platformer')

#load images
bg_img = pygame.image.load(img/bg.png)
sun_img = pygame.image.load(sun.png)

# This code makes it that the screen stays on for more than 1 second
run = true 
# Adds a code that only works if it is on and will stay on till it is off
while run:

  screen.blit(img/bg_img, (0,0))
  screen.blit(img/sun_img, (100,100))

  pygame.display.update()

# Makes you be able to close the screen
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      # Closes it
      run = false

  pygame.quit()




