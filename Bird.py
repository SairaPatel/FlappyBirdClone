import pygame
from pygame.locals import *
from math import *

class Bird(pygame.sprite.Sprite):
     def __init__(self, x, y, width, height):
          self.width = width
          self.height = height
          self.x = x
          self.y = y
          
          self.score = 0

          self.jump_count = 0
          super().__init__()

          # sprite img
          self.img1 = pygame.image.load("images/downflap.png").convert_alpha()
          self.img2 = pygame.image.load("images/midflap.png").convert_alpha()
          self.img3 = pygame.image.load("images/upflap.png").convert_alpha()

          
          self.image = self.img1
          self.rect = self.image.get_rect()

          # scale image
          ratio = self.rect.width/self.rect.height

          self.images = [
               pygame.transform.scale(self.img1, (floor(self.height * ratio), self.height)),
               pygame.transform.scale(self.img2, (floor(self.height * ratio), self.height)),
               pygame.transform.scale(self.img3, (floor(self.height * ratio), self.height)),
               ]

          self.cos = 0
          self.cos_dir = +1
          self.image = self.images[self.cos]
          
          
          self.rect.x = self.x
          self.rect.y = self.y

          

     def set_cos(self):

          if self.cos == 0:
               self.cos_dir = +1
          elif self.cos == 2:
               self.cos_dir = -1
               
          
          self.cos += self.cos_dir

          
          if 0 < self.jump_count <= 3:
               self.image = self.images[0]
          elif 3 < self.jump_count <= 6:
               self.image = self.images[1]
          elif 6 < self.jump_count <= 10:
               self.image = self.images[2]

          

          
          if -65 < self.jump_count < -15:
               self.image = pygame.transform.rotate(self.images[0], self.jump_count *2 + 15)
          elif self.jump_count < -60:
               self.image = pygame.transform.rotate(self.images[0], 90)


          self.rect.width = self.image.get_rect().width
          self.rect.height = self.image.get_rect().height
         
                         

     def move(self, fps):
          # update y pos
          self.jump_count -= 1
          if self.jump_count > 0:
               
               self.rect.y -= floor(self.width/6)
          else:
               self.rect.y += 2 * abs(self.jump_count) * 0.13


          self.set_cos()

          
  