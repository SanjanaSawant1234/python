from random import randint
dice=randint(1,6)
guess=int(input("Guess the number:"))
if guess==dice:
    print("woho got lucky")
else:
    print("better luck next tym")





