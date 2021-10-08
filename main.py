from random import randint

# cpu = 
player_count = 0

options = ['1', '2', '3','4', '5', '6', '7', '8', '9', '10']
index = randint(1, 10)

while player_count <= 3:
    selection = input('1,2,3,4,5,6,7,8,9,10')
    
    if selection == options[index]:
        print("You guessed " + options[index] + " You win!")
        break
    elif(int(selection) > index):
        player_count += 1
        print('You guessed too high, try again')
        
    elif(int(selection) < index):
        player_count += 1
        print('You guessed too low')
       
    else: 
        print("You didnt guess " + options[index] + " Game Over!", player_count, "guesses too many")
        break