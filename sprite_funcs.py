import pygame
from pygame.locals import *

from math import *

class bird_class(pygame.sprite.Sprite):
     def __init__(self, x, y, width, height):
          self.width = width
          self.height = height
          self.x = x
          self.y = y
          
          self.score = 0

          self.jump_count = 0
          super().__init__()

          # sprite img
          self.img1 = pygame.image.load("downflap.png").convert_alpha()
          self.img2 = pygame.image.load("midflap.png").convert_alpha()
          self.img3 = pygame.image.load("upflap.png").convert_alpha()

          
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

          
     
class pipe_class(pygame.sprite.Sprite):
     def __init__(self, x, y_top, main_height, collar_height, collar_width, WIDTH, GROUND_HEIGHT, dark_green, light_green, green, highlight_col):

          self.x = x
          self.y_top = y_top
          self.main_height = main_height

          self.collar_height = collar_height

          # COLOURS
          white = pygame.Color(255, 255, 255)
          black = pygame.Color(0, 0, 0)

          # collar
          self.collar_width = collar_width
          
          # main pipe
          self.main_width = (self.collar_width * 0.8)

          self.height = self.main_height + self.collar_height

          # ypos
          if self.y_top:
               self.y = 0
          else:
               self.y = floor(GROUND_HEIGHT/2) + floor(GROUND_HEIGHT/2 - self.height)
          
          super().__init__()
          # image
          self.image = pygame.Surface((self.collar_width, self.height))
          self.rect = self.image.get_rect()
          self.image.fill(white)

          self.rect.x = self.x
          self.rect.y = self.y

          
          # create shape
          if y_top:
               collar_rect = pygame.Rect(0, self.height - self.collar_height, self.collar_width, self.collar_height)
               main_rect = pygame.Rect(floor((self.collar_width - self.main_width)/2), 0, self.main_width, self.main_height)
          else:
               collar_rect = pygame.Rect(0, 0, self.collar_width, self.collar_height)
               main_rect = pygame.Rect(floor((self.collar_width - self.main_width)/2), self.collar_height, self.main_width, self.main_height)

          # pipe fill
          pygame.draw.rect(self.image, green, collar_rect)
          pygame.draw.rect(self.image, green, main_rect)

          main_start = floor((self.collar_width - self.main_width)/2)
          main_end = self.collar_width - floor((self.collar_width - self.main_width)/2)

          
          # MAIN PIPE --------------------------------------------------------
          # main pipe shadows/highlights
          self.draw_shadow_reflections(main_start, main_end, 0, self.collar_height, self.main_height, dark_green, light_green, green, highlight_col)

          # collar pipe shadows/highlights
          self.draw_shadow_reflections(0, self.collar_width, self.main_height, 0, self.collar_height, dark_green, light_green, green, highlight_col)
          
          # pipe black outline
          outline_main_rect = main_rect
          outline_collar_rect = collar_rect
          
          if y_top:
               outline_collar_rect.height -= 1
          outline_collar_rect.width -= 1
          
          pygame.draw.rect(self.image, black, outline_collar_rect, 2)
          pygame.draw.rect(self.image, black, outline_main_rect, 2)


          # remove background
          self.image.set_colorkey(white)



     def draw_shadow_reflections(self, start, end, top_y, btm_y, height, dark_green, light_green, green, highlight_col):
          
          # MAIN PIPE --------------------------------------------------------
          
          # main pipe dark shadow thick
          width1 = floor(self.main_width*0.2)
          if self.y_top:
               shadow_rect =  pygame.Rect(end - width1, top_y, width1,height)
          else:
               shadow_rect = pygame.Rect(end - width1, btm_y, width1, height)

          pygame.draw.rect(self.image, dark_green, shadow_rect) 


          # main pipe dark shadow thin
          width2 = floor(self.main_width*0.07)
          if self.y_top:
               shadow_rect2 =  pygame.Rect(end - (width1 + width2*3), top_y, width2, height)
          else:
               shadow_rect2 = pygame.Rect(end - (width1 + width2*3), btm_y, width2, height)

          pygame.draw.rect(self.image, dark_green, shadow_rect2) 

          # main pipe highlight thick
          width1 = floor(self.main_width*0.3)
          if self.y_top:
               highlight_rect1 =  pygame.Rect(start, top_y, width1, height)
          else:
               highlight_rect1 = pygame.Rect(start, btm_y, width1, height)

          pygame.draw.rect(self.image, light_green, highlight_rect1) 


          # main pipe highlight thin
          width2 = floor(self.main_width*0.07)
          if self.y_top:
               highlight_rect2 =  pygame.Rect(start + width1 + width2, top_y, width2, height)
          else:
               highlight_rect2 = pygame.Rect(start + width1 + width2, btm_y, width2, height)

          pygame.draw.rect(self.image, light_green, highlight_rect2) 





     

     def move(self, screen_width, bird, pipes):

               # move pipe along
               self.rect.x -= 1
               
               # reset pipe's size and pos
               if self.rect.x < -self.rect.width:
                    return False
               
               # if past pipe, increase score
               if bird.rect.x + bird.rect.width == self.rect.x and self.y_top:
                    bird.score += 1

          




     











          
          
