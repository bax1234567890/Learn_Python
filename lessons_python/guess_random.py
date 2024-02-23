import random

print('Hello, what is your name')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1  and 20')
secretNumber = random.randint(1, 20)
print('DEBUG: Secret number is ' + str(secretNumber))

for guessTaken in range(1, 7):
    while True:  # Ensures we keep asking for a guess until a valid input is received
        print('Take a guess.')
        try:
            guess = int(input())  # Attempt to convert the input to an integer
            break  # Exit the loop if the conversion was successful
        except ValueError:  # Catches non-integer inputs specifically
            print('Please enter a valid integer.')  # Prompt again if the conversion fails


    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for correct number!

if guess == secretNumber:
    print('Good job, ' + name + '! You guess my number in ' + str(guessTaken) +' guess!')
else:
    print('Nope, the number I was thinking is ' + str(secretNumber))