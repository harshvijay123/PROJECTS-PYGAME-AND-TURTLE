import itertools as it
def Change(index,player_moves,turn):
    win_combinations=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    permutations=list(it.permutations(player_moves,3))
    global lst
    if turn%2==0:
        lst[index]='O'
    else:
        lst[index]='X'
    for i in win_combinations:
        if i in permutations:
            return True
def draw(board):
    l=[]
    for i in board:
        l.append(i)
        if len(l)==3:
            print(' '.join(l))
            l=[]
    print('\n')

    
lst=list('_'*9)
player1=[]
player2=[]
win=False

draw(lst)

for chance in range(9):
    if chance%2==0:
        choice=int(input('player 1: '))-1
        player1.append(choice)
        if Change(choice,player1,chance):
            draw(lst)
            print('player 1 won..!'.center(115,'_'))
            win=True
            break
    else:
        choice=int(input('player 2: '))-1
        player2.append(choice)
        if Change(choice,player2,chance):
            draw(lst)
            print('player 2 won..!'.center(115,'_'))
            win=True
            break
    draw(lst)        
        
if not win:
    print('Draw'.center(115,'_'))
        

        
