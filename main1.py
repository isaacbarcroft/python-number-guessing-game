from random import randint


cpu_count = 0

while cpu_count < 3 or selection == options[index]:
    selection = input('1,2,3,4,5,6,7,8,9,10')
    options = ['1', '2', '3','4', '5', '6', '7', '8', '9', '10']
    index = randint(0, 9)
    print(options[index])
    if selection == options[index]:
        print("Computer guessed your number, You lose")
        play_again = input ("Would you like to play again? Y/N ")
        if play_again.lower() == "y":
            print(cpu_count)
            cpu_count = 0
    else: 
        cpu_count = cpu_count + 1
        if cpu_count == 3:
            print('You win!')
            play_again = input ("Would you like to play again? Y/N ")
            if play_again.lower() == "y":
                cpu_count = 0