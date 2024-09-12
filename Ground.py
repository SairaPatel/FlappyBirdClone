import pygame, random
from pygame.locals import *
from math import *
from Pipe import Pipe


class Ground(pygame.sprite.Sprite):
     def __init__(self, x, y, width, height, dark_green, light_green, green, highlight_col, dirt_col, dirt_shadow_col):
          self.x = x
          self.y = y
          self.width = width
          self.height = height
          super().__init__()

          # create image
          self.image = pygame.Surface((self.width, self.height))
          self.rect = self.image.get_rect()
          self.rect.x = self.x
          self.rect.y = self.y
          
          self.image.fill(green)


          # TOP BAR
          top_bar = pygame.Rect(0, floor(self.height*0.05), self.width, floor(self.height*0.1))
          line_width =  floor(self.height*0.025)
          
          # draw diagonal line pattern
          line_gap = floor(top_bar.width/20)
          
          for n in range(0, top_bar.width, line_gap):
               pygame.draw.line(self.image, light_green, (n, top_bar.y + top_bar.height + 10), (n +line_gap, top_bar.y - 10), floor(line_gap/2))
               
          # draw bottom dirt
          pygame.draw.rect(self.image, dirt_col, (0, top_bar.y + top_bar.height , self.rect.width, self.rect.height))

          # draw top black line
          pygame.draw.line(self.image, (30,30,0), (- 10, 0), (top_bar.width + 10, 0), line_width)

          # draw top highlight line
          pygame.draw.line(self.image, highlight_col, (- 10, line_width), (top_bar.width + 10, line_width), line_width)

           # draw bottom  green shadow
          pygame.draw.line(self.image, dark_green, (- 10, top_bar.y + top_bar.height), (top_bar.width + 10, top_bar.y + top_bar.height), line_width)

          # draw bottom dirt shadow
          pygame.draw.line(self.image, dirt_shadow_col, (- 10, top_bar.y + top_bar.height + line_width), (top_bar.width + 10, top_bar.y + top_bar.height + line_width), line_width)

          
          
     def move(self, screen_width):
          
          self.rect.x -= 1
          if self.rect.x < -screen_width:
               self.rect.x = screen_width




