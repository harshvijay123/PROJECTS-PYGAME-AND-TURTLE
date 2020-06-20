from tkinter import *
import itertools as it
from tkinter import messagebox



def check_for_win(l):
    '''this function takes a list of player\'s-pressed-button-position and return True if it\'s any permutation
matches with the wining-combinations'''
    
    win_combinations=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    perm=list(it.permutations(l,3))
    for i in win_combinations:
        if i in perm:
            return True

def place_X_or_O(t,tu):
    '''this functions takes a turn-variable and tuple of grid position and make a label on it
according to turn variable and at the end change turn variable to the not(turn)'''
    
    global turn
    turn=tu
    l=Label(root,text='X' if turn else 'O',bg='black',fg='springgreen',font=('Comic Sans MS',40),padx=0,pady=0)
    l.grid(row=t[0],column=t[1],sticky='nswe',padx=2,pady=2)
    player1.append(t[2]) if turn else player2.append(t[2])

    global play1,play2   
    if turn:
        play1.destroy()
        play2=Label(root,text='PLAYER 2',bg='springgreen',font=('Arial',10,'bold'),padx=0,pady=0)
        play2.grid(row=3,column=2,sticky='nswe',padx=2,pady=2)
        
        
    else:
        play2.destroy()
        print(play2)
        play1=Label(root,text='PLAYER 1',bg='springgreen',font=('Arial',10,'bold'),padx=0,pady=0)
        play1.grid(row=3,column=0,sticky='nswe',padx=2,pady=2)
        
    turn=not(tu)
    if len(player1)>2 and check_for_win(player1):
        messagebox.showinfo('WINNER','player 1 won')
        START()
    elif len(player2)>2 and check_for_win(player2):
        messagebox.showinfo('WINNER','player 2 won')
        START()
    elif (len(player1)==5 and len(player2)==4) or (len(player2)==5 and len(player1)==4):
        messagebox.showinfo('TIE','TIE')
        START()
    
    
def Make_play_board():
    '''this function make a play board after clicking on play button and bind the busston with the
function make_X_or_O function'''

    
    global play1
    k=0
    start_b['state']='disabled'
    
    for i in range(3):
        for j in range(3):
            b=Button(root,text=' ',height=7,width=7,bg='black',fg='springgreen',activebackground='mediumspringgreen',
                     activeforeground='black',command=lambda t=(i,j,k):place_X_or_O(t,turn))
            b.grid(row=i,column=j,sticky='nswe',padx=2,pady=2)
            k+=1    
        
    play1=Label(root,text='PLAYER 1',bg='springgreen',font=('Arial',10,'bold'),padx=0,pady=0)
    play1.grid(row=3,column=0,sticky='nswe',padx=2,pady=2)
        
        


def START():
    '''this function starts our first interface that has a play-button and some labels of playing board structure'''
    global start_b,turn,player1,player2
    player1=[]
    player2=[]

    turn=True
        
    for i in range(3):
        for j in range(3):
            l=Label(root,text=' ',height=7,width=7,bg='black',fg='springgreen')
            l.grid(row=i,column=j,sticky='nswe',padx=2,pady=2)

    start_b=Button(root,text='PLAY',command=Make_play_board,bg='black',fg='springgreen',
                 activebackground='mediumspringgreen',activeforeground='black',font=('Arial',40,'bold'),padx=0,pady=0)
    start_b.grid(row=3,columnspan=3,sticky='nswe',padx=2,pady=2)


if __name__=='__main__':
    root=Tk()
    root.resizable(False,False)
    for i in range(4):
        root.grid_rowconfigure(i,weight=1)
    for i in range(3):
        root.grid_columnconfigure(i,weight=1)
        
    root.configure(bg='springgreen')
    root.geometry('600x600+200+30')
    root.title('TIC TAC TOE')

    START()
    root.mainloop()
