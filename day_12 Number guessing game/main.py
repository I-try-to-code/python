import random 
n = random.randint(1, 99)
def game(x): #here the x defines the number of guesses that the user has 
    for i in range(x):
        print("You have", x-i, "guesses left")
        g= int(input("Make a guess: "))
        if g < n:
            print("Your guess is low")
        elif g > n:
            print("Your guess is high")
        else:
            print("You guessed it!")
            break
        
print("Welcome to the number guessing game\n\n RULES:\nYou have to guess the numebr that i am thinking.\n HINT: The number lies between 1-100")
diff=  input("Enter the difficulty leve; 'easy' or 'medium' or 'hard': ").lower()
if diff == 'easy':
    game(10)
elif diff == 'medium':
    game(7)
else:
    game(5)

