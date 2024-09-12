import pygame, random
from math import *

from Pipe import Pipe

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

                    
                         
          pipe1 = Pipe(x, True, height1, collar_height, collar_width,  WIDTH, GROUND_HEIGHT, dark_green, light_green, green, highlight_col)
     
          # pipe 2
          height2 = pipe_space - height1
          pipe2 = Pipe(x, False, height2, collar_height, collar_width, WIDTH, GROUND_HEIGHT, dark_green, light_green, green, highlight_col)

     
          pipes.add(pipe1, pipe2)

     
     return pipes




     
