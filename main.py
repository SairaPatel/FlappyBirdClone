import pygame, sys
from pygame.locals import *
from math import *

from Bird import Bird
from Pipe import Pipe
from Ground import Ground
from setup_funcs import *

pygame.init()

# COLOURS
dark_green = pygame.Color(0, 150, 0)
green = pygame.Color(80, 225, 10)
light_green = pygame.Color(160, 255, 100)

highlight_col = pygame.Color(200, 255, 190)

dirt_col = pygame.Color(230, 220, 160)
dirt_shadow_col = pygame.Color(220, 180, 50)

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 50, 50)

bg_col = pygame.Color(190, 240, 255)
     
# HOME MENU
def home(score):
     # WINDOW SETUP ------------------------------------------------------------
     WIDTH = 300
     HEIGHT = 450
     win = pygame.display.set_mode((WIDTH, HEIGHT))
     pygame.display.set_caption("Flappy Bird - Home")

     clock = pygame.time.Clock()
     fps = 60

     # SPRITE GROUPS------------------------------------------------------------
     all_sprites = pygame.sprite.Group()

     
     # GAME LOOP ------------------------------------------------------------
     run = True
     while run:
          clock.tick(fps)
          win.fill(bg_col)

          # play btn
          play_btn = pygame.Rect(floor(WIDTH*0.3), floor(HEIGHT*0.7), floor(WIDTH*0.4), floor(HEIGHT*0.1))
          pygame.draw.rect(win, red, play_btn)
          draw_text(play_btn.center[0], play_btn.center[1], "PLAY", (255, 255, 255), 40, win)
          # play btn outline
          play_btn_outline = (play_btn.x + 2, play_btn.y + 2, play_btn.width - 4, play_btn.height - 4)
          pygame.draw.rect(win, white, play_btn_outline, 1)
          
          
          # EVENTS ---------------------------------------------
          for event in pygame.event.get():
               
               # QUIT BTN --------------------------------------
               if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
               if event.type == MOUSEBUTTONDOWN:
                    if play_btn.collidepoint(event.pos):
                         pygame.mouse.set_pos(floor(WIDTH/2), floor(HEIGHT*0.9)) # move mouse so that it is no longer on play btn
                         run = False

               if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         run = False
                    if event.key == K_p:
                         pygame.mouse.set_pos(floor(WIDTH/2), floor(HEIGHT*0.9)) # move mouse so that it is no longer on play btn
                         run = False
                         
               
                         


          # DISPLAY
          high_score = read_highscore()
          
          if score is not None:
               # game over msg
               draw_text(floor(WIDTH/2), floor(HEIGHT*0.4), "GAME OVER", (0,0,0), 40, win)
               # score text
               draw_text(floor(WIDTH/2), floor(HEIGHT*0.6), "SCORE: " + str(score), (0,0,0), 20, win)
               # high score
               

               if score > int(high_score):
                    write_highscore(score)
        

          # TITLE
          # Text outline
          draw_text(floor(WIDTH/2)-2, floor(HEIGHT*0.2)-2 , "FLAPPY BIRD", light_green, 50, win) # top left
          draw_text(floor(WIDTH/2)+2, floor(HEIGHT*0.2)+2 , "FLAPPY BIRD", black, 50, win) # btm right       
          
          draw_text(floor(WIDTH/2), floor(HEIGHT*0.2), "FLAPPY BIRD", green, 50, win) 
          

          # HIGH SCORE
          draw_text(floor(WIDTH/2), floor(HEIGHT*0.5), "HIGH SCORE: " + str(high_score) , black, 20, win)


          
          pygame.display.update()

     main()



# PAUSE GAME
def pause(win, WIDTH, HEIGHT):
     clock = pygame.time.Clock()
     fps = 60
     
     run = True
     while run:

          # DISPLAY
          clock.tick(fps)
          win.fill(bg_col)


          # PLAY BTB
          play_btn = pygame.Rect(floor(WIDTH*0.3), floor(HEIGHT*0.7), floor(WIDTH*0.4), floor(HEIGHT*0.1))
          pygame.draw.rect(win, red, play_btn)
          draw_text(play_btn.center[0], play_btn.center[1], "PLAY", white, 40, win)
          # play btn outline
          play_btn_outline = (play_btn.x + 2, play_btn.y + 2, play_btn.width - 4, play_btn.height - 4)
          pygame.draw.rect(win, white, play_btn_outline, 1)


          # TEXT
          draw_text(floor(WIDTH/2), floor(HEIGHT*0.2), "GAME PAUSED", black, 50, win)

          
          # EVENTS
          for event in pygame.event.get():
               if event.type == QUIT:
                    return False
               if event.type == MOUSEBUTTONDOWN:
                    if play_btn.collidepoint(event.pos):

                         run = False
               if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         run = False

          pygame.display.update()

     return True
                    

# PLAY GAME
def main():

     # WINDOW SETUP ------------------------------------------------------------
     WIDTH = 300
     HEIGHT = 450
     win = pygame.display.set_mode((WIDTH, HEIGHT))
     pygame.display.set_caption("Flappy Bird")

     clock = pygame.time.Clock()
     fps = 60

     # SPRITE GROUPS------------------------------------------------------------
     all_sprites = pygame.sprite.Group()
     grounds = pygame.sprite.Group()
     pipes = pygame.sprite.Group()

     # SPRITES ------------------------------------------------------------

     # grounds
     GROUND_HEIGHT = floor(HEIGHT*0.8)
     ground1 = Ground(0, GROUND_HEIGHT, WIDTH+1, HEIGHT - GROUND_HEIGHT, dark_green, light_green, green, highlight_col, dirt_col, dirt_shadow_col)
     ground2 = Ground(WIDTH, GROUND_HEIGHT, WIDTH+1, HEIGHT - GROUND_HEIGHT, dark_green, light_green, green, highlight_col, dirt_col, dirt_shadow_col)
     grounds.add(ground1, ground2)

     # bird
     width = floor(WIDTH*0.06)
     bird = Bird(floor(WIDTH*0.1), floor(GROUND_HEIGHT/2) - floor(width/2), width, width)
     all_sprites.add(bird)

     # pipes
     gap_height = bird.height*5
     pipes = create_pipe_pair(pipes, WIDTH, GROUND_HEIGHT, gap_height, dark_green, light_green, green, highlight_col, 10, bird)
     
     
     # GAME VARS
     pause_count = 0
     
     # GAME LOOP ------------------------------------------------------------
     run = True
     while run:
          clock.tick(fps)
          win.fill(bg_col)

          # create pause btn
          pause_btn = pygame.Rect(floor(WIDTH*0.02), floor(HEIGHT*0.9), floor(WIDTH*0.1), floor(HEIGHT*0.07))
          
          # EVENTS ---------------------------------------------
          for event in pygame.event.get():
               
               # QUIT BTN --------------------------------------
               if event.type == QUIT:
                    run = False
                    
               
               if event.type == KEYDOWN:

                    # PAUSE -----------------------------------------
                    if event.key == K_p:
                         stop = pause(win, WIDTH, HEIGHT)
                         if stop == False:
                              run = False
                         else:
                              pause_count = 4*fps
                    # KEY CLICK - BIRD MOVE -------------------------
                    else:
                         bird.jump_count = 10
                    
               # MOUSE CLICK
               if event.type == MOUSEBUTTONDOWN:
                    # PAUSE BTN CLICK --------------------------
                    if pause_btn.collidepoint(event.pos):
                         stop = pause(win, WIDTH, HEIGHT)
                         if stop == False:
                              run = False
                         else:
                              pause_count = 4*fps

                    #MOUSE CLICK - BIRD MOVE ----------------------
                    else:
                         bird.jump_count = 10

               

          if pause_count == 0:
               # MOVE BACKGROUND
               for ground in grounds.sprites():
                    ground.move(WIDTH)
               

               # MOVE PIPES and update score
               create_new = False
               for pipe in pipes.sprites():

                    # check if pipes reached end
                    if pipe.move(WIDTH, bird, pipes) == False:
                         pipes.remove(pipe)
                         create_new = True

               if create_new:
                    pipes = create_pipe_pair(pipes, WIDTH, GROUND_HEIGHT, gap_height, dark_green, light_green, green, highlight_col, 1, bird)
          

               # UPDATE BIRD POS
               bird.move(fps)
               

          # FLOOR COLLISION
          if bird.rect.y + bird.rect.height > ground1.y:
               run = False


          # PIPE COLLISION
          for pipe in pipes.sprites():
               if pygame.sprite.collide_mask(pipe, bird) is not None:
                    run = False


         
          # DRAW
          # display sprites
          all_sprites.draw(win)
          grounds.draw(win)
          pipes.draw(win)
          
          # display score
          draw_text(floor(WIDTH/2), floor(HEIGHT*0.2), str(bird.score), black, 30, win)

          # display pause btn
          pygame.draw.rect(win, red, pause_btn)
          draw_text(pause_btn.center[0], pause_btn.center[1], "I I", white ,20, win)
          
          pause_btn_outline = (pause_btn.x + 2, pause_btn.y + 2, pause_btn.width - 4, pause_btn.height - 4)
          pygame.draw.rect(win, white, pause_btn_outline, 1)
          
          
           # display pause count
          if pause_count > 0:
               pause_count -=1

               draw_text(floor(WIDTH/2), floor(HEIGHT*0.92), str(floor(pause_count/fps)), black, 50, win)

          
          pygame.display.update()
          

     home(bird.score)        

home(None)







