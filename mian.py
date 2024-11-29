
'''We all have played snake, water gun game in our childhood. If you haven’t, google the 
rules of this game and write a python program capable of playing this game with the 
user. '''

'''
1 for snake 
-1 for waater
0 for gun
'''

import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer.

print(f"You Chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")

if(computer == you):   
    print("Its a Drow")
else:
    if(computer== -1 or you== 1):  
        print("You Win")
        
    elif (computer== -1 or you== 0):
            print("You lose")
            
    elif (computer== 1 or you== -1):
                print("You lose")
                
    elif (computer== 1 or you== 0):
              print("You Win")
              
    
    elif (computer== 0 or you== -1):
              print("You Win")
              
    
    elif (computer== 0 or you== 1):
              print("You Lose")
    
    else:
        print("Invalid Input")






