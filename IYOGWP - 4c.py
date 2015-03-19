# This is a guess the number game.
import random

guessesTaken = 0

print('Input the numbers you want to guess between: (Low first)')
minInt = input()
maxInt = input()

print('Also, how many guesses do you want:')
guessesRequested = input()
guessesRequestedInt = int(guessesRequested)

number = random.randint(int(minInt), int(maxInt))
print('Well, I am thinking of a number between ' + str(minInt) + ' and ' + str(maxInt))

while guessesTaken < guessesRequestedInt:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
