import random

countries = ['Pakistan', 'Japan', 'Turkey', 'India', 'England', 'Brazil', 'Canada']
animals = ['Elephant', 'Tiger', 'Kangaroo', 'Panda', 'Dolphin', 'Cheetah', 'Rabbit']
fruits = ['Apple', 'Banana', 'Mango', 'Strawberry', 'Pineapple', 'Orange', 'Grapes']

all_categories =[countries, animals, fruits]
category_names=['Countries', 'Animals', 'Fruits']

category_index=random.randint(0,len(all_categories)-1) 
word = random.choice(all_categories[category_index]).lower()
print(f"It is a '{category_names[category_index]}' category.")

attempts = len(word) + 2
current_state = ['-'] * len(word)
guessed_letters=set()

while True:
    if attempts==0:
        print(f'Out of attempts! The word was: {word}')
        break
    
    print(f'Attempts left: {attempts}')
    print("Word : "+''.join(current_state)) 
    
    guess = input('Enter a character: ').strip().lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print('Enter only one valid character')
        continue
    
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'.") 
        continue
    
    if guess in word:
        guessed_letters.add(guess) 
        for idx, ch in enumerate(word): ##japan
            if ch == guess:
                current_state[idx] = guess                                             
    else:
        print("Wrong guess!")
        attempts-=1    
    
    # If word is completely guessed
    if "-" not in current_state:
        print("You guessed the word:", ''.join(current_state))
        break