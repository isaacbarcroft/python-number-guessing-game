from random import randint

# cpu = 
player_count = 0

while player_count < 3:
    selection = input('1,2,3,4,5,6,7,8,9,10')
    options = ['1', '2', '3','4', '5', '6', '7', '8', '9', '10']
    index = randint(1, 10)
    print(options[index])
    if selection == options[index]:
        print("You win!")
    else: 
        print("you lose")
        player_count = player_count + 1
        if player_count == 3:
            print('Game Over!')