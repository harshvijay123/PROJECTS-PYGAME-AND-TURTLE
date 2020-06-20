import turtle
import random
import math
from tkinter import messagebox


#VARIABLES
speed=1
point=0
level=1
wn_pt=2
sc_width=800
sc_height=800
X=350
Y=350


#SETUP
wn=turtle.setup(sc_width,sc_height)
turtle.bgcolor('black')
h=turtle.Turtle()
h.pu()
h.setpos(-X,-Y)
h.pd()
h.color('white','springgreen')
h.begin_fill()
h.hideturtle()

#Winbox

def levelUpdate():
    global speed,level,wn_pt
    level+=1
    speed+=0.3
    wn_pt+=5
    
    l.clear()
    l.write('Level: '+str(level),font=50)
    
    
    
def win_box(PT):
    messagebox.showinfo('YOU WON...!','YOUR SCORE {}'.format(PT))
    levelUpdate()
    return
    
#playing board
for i in range(4):
    h.fd(2*X)
    h.lt(90)
h.end_fill()



#score board
l=turtle.Turtle()
l.pu()
l.setpos(-300,350)
l.color('blue')
l.ht()
l.write('Level: '+str(level),font=50)



h.pu()
h.setpos(230,350)
h.pd()
h.pensize(5)
for i in range(2):
    h.fd(140)
    h.lt(90)
    h.fd(40)
    h.lt(90)
h.pu()
h.color('blue')
h.setpos(240,360)
h.pd()
h.write('SCORE : ',font=30)

s=turtle.Turtle()
s.hideturtle()
s.color('lightgreen')
s.pu()
s.setpos(330,360)
s.pd()
s.write('0',font=20)
def score_update(score):
    s.clear()
    s.write(str(score),font=20)


#PLAYER TURTLE
player=turtle.Turtle()
player.shape('turtle')
player.pu()
player.color('black')
#player.lt(90)




#FOOD TURTLE
food=turtle.Turtle()
food.shape('circle')
food.pu()
food.speed(0)
def make_food():
    global a,b
    a=random.randint(-330,330)
    b=random.randint(-330,330)
    food.clear()
    food.color('blue')
    food.setpos(a,b)
    
make_food()

#TURTLE MOVEMENT FUNCTIONS
def turnLeft():
    player.lt(20)
    return
def turnRight():
    player.rt(20)
    return
def speedUp():
    global speed
    speed+=0.1
    return
def speedDown():
    global speed
    if speed>1:
        speed-=0.1
    return
#BINDING OF FUNCTIONS
turtle.listen()
turtle.onkey(turnLeft,'Left')
turtle.onkey(turnRight,'Right')
turtle.onkey(speedUp,'Up')
turtle.onkey(speedDown,'Down')



while True:
    player.fd(speed)
    #food.fd(0.5)
    x,y=player.position()
    #a,b=food.position()
    if x>X :
        player.speed(0)
        player.setpos(x-2*X,y)
    if x<-X :
        player.speed(0)
        player.setpos(x+2*X,y)
    if y>Y :
        player.speed(0)
        player.setpos(x,y-2*Y)
        
    if y<-Y :
        player.speed(0)
        player.setpos(x,y+2*Y)

    #CHECKING FOR FOOD
    '''we are calculating distance for collision detection'''
    d=math.sqrt((x-a)**2+(y-b)**2)
    
    if d<20:
        point+=1
        score_update(point)
        make_food()
        
    if point>wn_pt:
        win_box(point)
        

turtle.done()
     


    
