import pygame

pygame.init()


screenH = 540
screenW = 960
screen = pygame.display.set_mode((screenH, screenW))

bird_images = [pygame.image.load("images/Bird_neutral.png"), 
               pygame.image.load("images/Bird_fall.png"),
               pygame.image.load("images/Bird_flap.png")]

BG_images = [pygame.transform.scale(pygame.image.load("images/BG_day.png"), (screenH, screenW))]

Pipe_images = [pygame.image.load("images/Pipe_down.png"),
               pygame.image.load("images/Pipe_up.png")]

Ground_image = pygame.image.load("images/Ground.png")



## GAME SETTINGS
fps = 30
max_score = 100
score = 1
running = True
## BIRD SETTINGS
bird_velocity = 5
max_drop_angle = -90
max_jump_angle = 90
## GROUND SETTINGS
ground_velocity = 5
ground_start_posY = screenW

## PIPE SETTINGS





class Ground:
    IMGS = [Ground_image, Ground_image, Ground_image]
    velocity = ground_velocity
    GroundW = Ground_image.get_width()

    def __init__(self, ground_start_posY):
        self.x1 = 0
        self.x2 = self.GroundW
        self.x3 = self.GroundW * 2
        self.y = ground_start_posY

    def move(self):
        self.x1 -= self.velocity
        self.x2 -= self.velocity
        self.x3 -= self.velocity

        if self.x1 + self.GroundW < 0:
            self.x1 = self.x3 + self.GroundW
        if self.x2 + self.GroundW < 0:
            self.x2 = self.x1 + self.GroundW
        if self.x3 + self.GroundW < 0:
            self.x3 = self.x2 + self.GroundW
            
class Bird:
    def __init__(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
        self.velocity = bird_velocity
        self.angle = 0
        self.img = bird_images
        self.time = 0
    def move(self):
        self.time += 1
        print()
    def jump(self):
        print()

class Pipe:
    def __init__():
        print()

while running == True:
    screen.blit(BG_images[0], (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(BG_images[0], (0,0))

    pygame.display.flip()
    
    

pygame.quit()