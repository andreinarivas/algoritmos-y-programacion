import random

dice=[1,2,3,4,5,6]
name_p1=input('Please enter P1 name: \n >>> ').upper()
name_p2=input('Please enter P2 name: \n >>> ').upper()
turn=1
turn_p1=True
roll_p1=0
points_p1=0
turn_p2=True
roll_p2=0
points_p2=0
while turn<=7:
    print("TURN {}\n".format(turn))
    while turn_p1==True:
        roll_p1= random.choice(dice)
        print('Player {} rolled a {}\n'.format(name_p1,roll_p1))
        if roll_p1==1:
            points_p1+=10
        elif roll_p1==2:
            points_p1+=20
        elif roll_p1==4:
            points_p1*=2
        elif roll_p1==5:
            points_p1+=40
        elif roll_p1==6:
            points_p1/=2
        else:
            print('Player rolls again\n')
            continue
        turn_p1=False
    print('Player {} score is {} points\n'.format(name_p1,points_p1))
    while turn_p2==True:
        roll_p2= random.choice(dice)
        print('Player {} rolled a {}\n'.format(name_p2,roll_p2))
        if roll_p2==1:
            points_p2+=10
        elif roll_p2==2:
            points_p2+=20
        elif roll_p2==4:
            points_p2*=2
        elif roll_p2==5:
            points_p2+=40
        elif roll_p2==6:
            points_p2/=2
        else:
            print('Player rolls again \n')
            continue
        turn_p2=False
    print('Player {} score is {} points\n'.format(name_p2,points_p2))
    turn_p2=True
    turn_p1=True
    turn+=1
print('Player 1 scored a total of {} points \n Player 2 scored a total of {} points\n'.format(points_p1,points_p2))
if points_p2>points_p1:
    print("Player {} won".format(name_p2))
elif points_p1>points_p2:
    print('Player {} won'.format(name_p1))
else:
    print('It was a draw between player {} and player {}'.format(name_p1,name_p2))
