import random

computer = random.randint(-1,1)

dict= {"snake":1, "water":0, "gun":-1}
    

rev = {}
for key in dict:
    rev[dict[key]] = key

youstr = input("enter your choice out of snake, water and gun :")
you = dict[youstr]
print(f"computer chose {rev[computer]} \nyou chose {youstr}")
if computer == you:
    print("it is a draw")
else :
    if computer== -1 and you ==0:
        print("you win!")
    elif computer== -1 and you ==1:
        print("you loose!")
    elif computer == 1 and you == -1:
        print("you loose!")
    elif computer ==1 and you ==0:
        print("you win!")
    elif computer ==0 and you == -1:
        print("you loose!")
    elif computer == 0 and you == 1:
        print("you win!")
    

