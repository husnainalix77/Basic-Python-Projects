import random

def addWord(letter, word, current_state):
    'Adds word if it is valid letter'
    
    if letter in word:       
        for idx, ch in enumerate(word): ##japan
            if ch == letter:
                current_state[idx] = letter
        return True 
    return False            

## Main Program    
if __name__ == "__main__":
    countries = ['Pakistan', 'Japan', 'Turkey', 'India', 'England', 'Brazil', 'Canada']
    animals = ['Elephant', 'Tiger', 'Kangaroo', 'Panda', 'Dolphin', 'Cheetah', 'Rabbit']
    fruits = ['Apple', 'Banana', 'Mango', 'Strawberry', 'Pineapple', 'Orange', 'Grapes']

    all_categories =[countries, animals, fruits]
    category_names=['Countries', 'Animals', 'Fruits']
    while True:    

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
            
            print(f'\nAttempts left: {attempts}')
            if len(guessed_letters)>=1:
                print(f"Guessed letters so far:{', '.join(sorted(guessed_letters))}")
                
            print("Word : "+' '.join(current_state)) 
            
            guess = input('Enter a character: ').strip().lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print('Enter only one valid character')
                continue
            
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'.") 
                continue
            
            if addWord(guess, word, current_state):
                print(f"Good guess! '{guess}' is in the word.")
                                                                
            else:
                print("Wrong guess!")
                attempts-=1    
                
            guessed_letters.add (guess)   
            
            # If word is completely guessed
            if '-' not in current_state:
                print("Word : "+''.join(current_state)) 
                print("You guessed the word:", ''.join(current_state).upper())
                break ## To break inner loop
            
        op=input('Do you want to play again (yes/no): ').strip().lower()
        if op == 'no':
            print('Thanks for playing!')
            break ## to break outer loop
        
