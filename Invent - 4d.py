import random

guessesTaken = 0

print('Hello! You are going to guess a letter, how many guesses do you want?')
amount = input()

randLetterSelector = random.randint(0, 25)
alphabet = ('abcdefghijklmnopqrstuvwxyz')
randLetter = alphabet[randLetterSelector]
print(randLetter)

print('Ok, I\'ve picked a letter.')

while guessesTaken < int(amount):
    print('Take a guess.')
    guess = input()

    guessesTaken = guessesTaken + 1

    if alphabet.index(guess.lower()) < alphabet.index(randLetter):
        print('Your guess is too close to A')

    if alphabet.index(guess.lower()) > alphabet.index(randLetter):
        print('Your guess is too close to Z')

    if guess.lower() == randLetter:
        break

if guess.lower() == randLetter:
    guessesTaken = str(guessesTaken)
    print('Good job! You guessed my letter in ' + guessesTaken + ' guesses!')

if guess.lower() != randLetter:
    print('Nope. The letter I was thinking of was ' + randLetter)
