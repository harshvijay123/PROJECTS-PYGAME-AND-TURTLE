import pygame

pygame.init()

display_width=400
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('fisrt game')


x=50
y=425
width=40
height=60
val=5
r=20





clock=pygame.time.Clock()


run=False


while not run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=True

            
    # this will Quit the game if the object colide with wall
    
    if x>=display_width-r or x<=r or y<=r or y>=display_height-r:
        run=True



    # for movement of the object
    
    keys=pygame.key.get_pressed()
    
    #for horizontal move
    
    if keys[pygame.K_LEFT] and x>r:
        x-=val
    if keys[pygame.K_RIGHT] and x<display_width-r:
        x+=val

    # for vertical move
    
    if keys[pygame.K_UP] and y>r:
        y-=val
    if keys[pygame.K_DOWN] and y<display_height-r:
        y+=val

    gameDisplay.fill((0,0,0))

    pygame.draw.circle(gameDisplay,(255,255,255),(x,y),r)# put a circle
   


    
   

    
    pygame.display.update()
    clock.tick(100)


pygame.quit()
quit()
