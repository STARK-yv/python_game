import random
print("1 : ROCK ; 2 : PAPER ; 3 : SCISSOR")
x=' '
while not (x==1 or x==2 or x==3):
    x=int(input("Choose any one to play ! : "))
print("(Your Move) : (Computer's Move)")
y=random.randint(1,3)
if y==1:
    if x==1:
        print("Game is DRAW , ROCK : ROCK")
    elif x==2:
        print("You WIN , PAPER : ROCK")
    else:
        print("You LOOSE , SCISSOR : ROCK")
if y==2:
    if x==1:
        print("You LOOSE , ROCK : PAPER")
    elif x==2:
        print("Game is DRAW , PAPER : PAPER")
    else:
        print("You WIN , SCISSOR : PAPER")
if y==3:
    if x==1:
        print("You WIN , ROCK : SCISSOR")
    elif x==2:
        print("You LOOSE , PAPER : SCISSOR")
    else:
        print("Game is DRAW , SCISSOR : SCISSOR")




