import random

'''
1 for rock
-1 for paper
0 for scisor
'''

computer = random.choice([1,-1,0])

youstr = input("Enter your choice: ")
youdict = {"r": 1, "p": -1, "s": 0}
you = youdict[youstr]
reversedict = {1: "rock", -1: "paper", 0: "scisor"}

print(f"you chose {reversedict[you]}\ncompuetr chose {reversedict[computer]}")

if(computer==you):
    print("its draw")
else:
    if(computer==1 and you==-1):
        print("You win")

    elif(computer==1 and you==0):
        print('You lose')

    elif(computer==-1 and you==0):
        print('You win')

    elif(computer==-1 and you==1):
        print('You lose')

    elif(computer==0 and you==1):
        print('You win')

    elif(computer==0 and you==-1):
        print('You lose')

    else:
        print("something went wrong")


    
        
