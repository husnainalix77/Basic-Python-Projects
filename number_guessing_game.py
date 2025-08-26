import random
x = random.randint(0,100)
print("I have selected a number between 0 and 100.")
n = eval(input("Guess what is it:"))

guess = 1

while(n != x):
    print("No, it's wrong!")
    if(x > n):
        print(f"No, it's above {n}")
        
    else:
        print(f"No, it's below {n}")
        
    n=eval(input("Guess again:"))
    guess += 1
    
print("Yes, you guessed it right")
print(f"You tried {guess} times to guess the number") 