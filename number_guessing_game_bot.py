import random

def numberguessbot(low, high):
    user_response = " "
    trial_count = 0
    
    while user_response != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        trial_count += 1
        print(f"\nGuess #{trial_count}: {guess}")
        user_response = input("Is the number higher (H) or lower (L) or correct (C)? ").lower()
        
        if user_response == 'h':
            low = guess + 1
        elif user_response == 'l':
            high = guess - 1
    
    print(f"\nThank you for playing!! \nI guessed the number as {guess} correctly in {trial_count} guesses")
    
print("This game allows the user to think of a random number in a given range and attempts to guess it")    
low = int(input("Enter the min value of range: "))
high = int(input("Enter the max value of range: "))
numberguessbot(low, high)
