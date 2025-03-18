import pygame
import datetime
import time

def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)  
    surf.blit(rotated_image, new_rect)


pygame.init()
pygame.display.set_caption("Mickey Clock")


screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
font = pygame.font.Font("task1/font/Pixeltype.ttf", 100)


mickey = pygame.image.load("task1/pics/main1.png").convert_alpha()
mickey = pygame.transform.scale(mickey, (800, 400))

right_hand = pygame.image.load("task1/pics/right-hand.png").convert_alpha()
right_hand = pygame.transform.scale(right_hand, (200, 200))

left_hand = pygame.image.load("task1/pics/left-hand.png").convert_alpha()
left_hand = pygame.transform.scale(left_hand, (200, 200))


clock_center = (400, 200)  

done = False

while not done:
   
    now = datetime.datetime.now()
    min = now.minute
    sec = now.second

   
    ang_min = -(6 * min + sec / 10) 
    ang_sec = -(6 * sec) 

   
    time_of_clock = now.strftime(r"%M:%S")
    text = font.render(time_of_clock, True, 'Green')
    text_rect = text.get_rect(topleft=(100, 200))  

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    screen.fill((255, 255, 255))
    screen.blit(mickey, (0, 0))

    blitRotateCenter(screen, right_hand, clock_center, ang_min)  
    blitRotateCenter(screen, left_hand, clock_center, ang_sec)  

    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()