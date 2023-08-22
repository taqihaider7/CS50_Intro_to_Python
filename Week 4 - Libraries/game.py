import random
# while loop
while True:
        try:  # accepting only positive integer
            n = int(input("Level: "))
            if n > 0:
                   break
        except:
               pass
number = random.randint(1,n)   # setting randomvalues
guess = 0
while True:
        try:
            guess = int(input("Guess: "))   # asking user for postive guess integer
            if guess > 0:
                if guess < number:
                    print("Too small!")
                elif guess > number:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        except:
             pass


