# Press on empty background to add new brick, press on the brick to remove

import pygame

class Brick: 
  def __init__(self, x, y) -> None:
    self.img = pygame.Surface( (BRICK_SIZE, BRICK_SIZE) )
    self.img.fill(BRICK_COLOR)
    self.rect = self.img.get_rect()
    self.rect = self.rect.move( [x, y])
    self.speed = [1, 1]

def find_brick(bricks, x, y) :
  index = -1
  for brick in bricks :
    index += 1
    if (x > brick.rect.left and x < brick.rect.right) and (y > brick.rect.top and y < brick.rect.bottom) :
      return index
  return -1
    
pygame.init()

HEIGHT = 640
WIDTH = 1280
BACKGROUND_COLOR = (0, 100, 100)
BRICK_COLOR = (255, 255, 255)
BRICK_SIZE = 80
FPS = 100

main_display = pygame.display.set_mode( (WIDTH, HEIGHT) )
main_display.fill( BACKGROUND_COLOR )
main_display_fps = pygame.time.Clock()

bricks = []
new_brick = Brick(0, 0)
bricks.append(new_brick)

playing = True
while playing :
  main_display_fps.tick(FPS)
  
  for event in pygame.event.get() :
    if event.type == pygame.QUIT :
      playing = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      pos=pygame.mouse.get_pos()
      btn=pygame.mouse
      
      index = find_brick(bricks, pos[0], pos[1])
      
      if index == -1: #add new
        new_brick = Brick(pos[0], pos[1])
        bricks.append(new_brick)
        FPS -= 10
      else : # remove
        bricks.pop(index)
        FPS += 10
  
  main_display.fill(BACKGROUND_COLOR)
  
  for brick in bricks:
    if brick.rect.right > WIDTH or brick.rect.left < 0 :
      brick.speed[0] = -brick.speed[0]
      
    if brick.rect.bottom > HEIGHT or brick.rect.top < 0 :
      brick.speed[1] = -brick.speed[1]
    
    main_display.blit(brick.img, brick.rect)
    brick.rect = brick.rect.move(brick.speed)
  
  pygame.display.flip()