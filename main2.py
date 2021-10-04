from random import randint




count = 1
num = int(input("Enter a number between 1- 100"))
low = 1
high = 100
guess = (low+high)//2 
while guess != num:
    guess = (low+high)//2
    print("the computer guesses...", guess)
    if guess > num: 
        high = guess
        count = count + 1
    elif guess < num:
        low = guess + 1
        count = count + 1
        
print("the computer guessed your number in", count, "tries")
    