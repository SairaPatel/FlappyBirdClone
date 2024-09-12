import pygame, sys, random
from pygame.locals import *

from math import *
from sprite_funcs import *

# TEXT
def draw_text(x, y, string, col, size, window):
     font = pygame.font.SysFont("Impact", size )
     text = font.render(string, True, col)
     textbox = text.get_rect()
     textbox.center = (x, y)
     window.blit(text, textbox)

     return textbox


def read_highscore():
     file = open("high_score.txt", "r")
     high_score = file.readlines()

     return high_score[0]

def write_highscore(score):
     file = open("high_score.txt", "w")
     file.write(str(score))

     

     
     
# FLOOR

class ground_class(pygame.sprite.Sprite):
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


def draw_floor(ground, WIDTH, HEIGHT, win, dirt_col, dirt_shadow_col):
     # BELOW GROUND LINE
     height = HEIGHT - (ground.rect.y + ground.rect.height)

     pygame.draw.rect(win, ())
     


def create_pipe_pair(pipes, WIDTH, GROUND_HEIGHT, gap_height, dark_green, light_green, green, highlight_col, add_num, bird):
     
     for n in range(add_num):

          # collar dimensions
          
          collar_width = floor(WIDTH*0.1)
          collar_height = floor(GROUND_HEIGHT*0.05)

          


          if len(pipes.sprites()) > 0:
               # change difficulty
               weighted_values = []
               if 0 < bird.score < 130:
                    prob_bound = WIDTH*(bird.score*0.1)
               elif bird.score > 130:
                    prob_bound = WIDTH*(130*0.1)
               else:
                    prob_bound = 0

               # weights depending on score
               for n in range(0, WIDTH):
                    if n > prob_bound:
                         weighted_values.append(2)
                    else:
                         weighted_values.append(1)
               
               # x position
               prev_x = pipes.sprites()[-1].rect.x
               gap = random.choices(range(0, WIDTH), weights = weighted_values, k = 1)[0]
               x = gap + prev_x + collar_width
          
          else:
               x = floor(WIDTH)
          
          # pipe 1
          pipe_space = GROUND_HEIGHT - (collar_height*2  + gap_height)
          min_height = gap_height

          repeat_height = True
          while repeat_height:
               height1 = random.randint(min_height, GROUND_HEIGHT - (min_height + collar_height*2))
     
               repeat_height = False
               # check if adjacent pipe gap, overlaps with current gap
               if len(pipes.sprites()) > 0 and gap < bird.rect.width:
                    if abs(height1 - pipes.sprites()[-2].rect.height) > bird.rect.height:
                         repeat_height = True

                    
                         
          pipe1 = pipe_class(x, True, height1, collar_height, collar_width,  WIDTH, GROUND_HEIGHT, dark_green, light_green, green, highlight_col)
     
          # pipe 2
          height2 = pipe_space - height1
          pipe2 = pipe_class(x, False, height2, collar_height, collar_width, WIDTH, GROUND_HEIGHT, dark_green, light_green, green, highlight_col)

     
          pipes.add(pipe1, pipe2)

     
     return pipes





