import random
def game_win(user,computer):
    if user == computer:
        return None
    #Snake vs water
    if user=="s" and computer == "w" :
        return True
    if user =="w"and computer=="s":
        return False

    #water vs gun
    if user=="w"and computer=="g":
        return True
    if user=="g"and computer=="w":
        return False
    
    #gun vs snake
    if user=="g" and computer== "s" :
        return True
    if user=="s" and computer == "g":
        return False   

rand_no=random.randint(1,3)
print("computer's turn : snake(s),water(w),gun(g)")
if rand_no==1:
    computer="s"
elif rand_no==2:
    computer="w"
else:
    computer="g"

user=input("your turn : snake(s),water(w),gun(g)").lower()
result=game_win(user,computer)#returns true if you win, false for lose none for draw..
print(f"\n you chose : {user}")
print(f"\n computer chose : {computer}")
if result is None:
    print("its a draw! ")
elif(result):
    print("You win! ")
else:
    print("You lose! ")                    