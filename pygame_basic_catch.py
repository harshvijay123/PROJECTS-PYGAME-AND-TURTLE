import pygame
from random import *
from tkinter import *



pygame.init()

display_width=400
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('fisrt game')



x=50
y=425
width=20
height=25
val=2
w,h=10,10
r=20
a,b=80,100





clock=pygame.time.Clock()


run=False
isJump=False
jumpcount=10
neg=-1


while not run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=True

            
    # this will Quit the game if the object colide with wall
    
    if x>=display_width-width or x<=0 or y<=0 or y>=display_height-height:
        run=True



    # for movement of the object
    
    keys=pygame.key.get_pressed()
    
    #for horizontal move
    
    if keys[pygame.K_LEFT] and x>=0:
        x-=val
    if keys[pygame.K_RIGHT] and x<display_width-width:
        x+=val

    # for vertical move
    
    if not (isJump):
        if keys[pygame.K_UP] and y>=0:
            y-=val
        if keys[pygame.K_DOWN] and y<display_height-height:
            y+=val
        if keys[pygame.K_SPACE]:  
            isJump=True            #  jumping

    else:
        
        if jumpcount >= -10:
            neg=1
            if jumpcount < 0:
                neg=-1
            y-=(jumpcount**2)//2*neg
            jumpcount-=1
            if ((a+w > x or x==a+w or x==a) and  not (x+width<a) ) and ((y==b or y==b+h or y<b+h) and not(y<b-height)):
                height+=5
                a=randint(50,350)
                b=randint(50,550)  
                
        else:
            isJump=False
            jumpcount=10

            
    if ((a+w > x or x==a+w or x==a) and  not (x+width<a) ) and ((y==b or y==b+h or y<b+h) and not(y<b-height))  : 
        height+=5
        a=randint(50,350)
        b=randint(50,550)
    
        
    gameDisplay.fill((0,0,0))

    pygame.draw.rect(gameDisplay,(255,255,255),(x,y,width,height))# put a head
    #pygame.draw.circle(gameDisplay,(255,0,0),(x,y),5)
    pygame.draw.rect(gameDisplay,(0,255,0),(a,b,w,h))
   


    
   

    
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()



