# This program is like used for online quizzes. It will pick
# MCQs from 3 different files labeled as# Easy, Medium and Hard. First MCQ
# should be from Medium file and if theuser answers it wrong then next should
# come from easy otherwise from hard.This pattern should continue up till the
# end of the quiz. The user shouldn’t beaware of what difficulty level a particular MCQ belongs to.
# Each difficulty level should have differentmarks.

def loadQuestions(file_name):
    questions = []
    'Loads all questions from a txt file'
    
    with open(file_name, 'r') as f:
        for i in f:
            q = i.strip().split('\t') ## Converting into a list
            questions.append(q)
    return questions         

def runQuiz():
    'Runs the quiz simulator'
    current_file = 'medium.txt'
    total_correct, total_wrong, total_marks = 0, 0, 0
    total_questions = 10
    asked = 0
    
    questions_bank ={ ## Loads all questions in respective files
        'easy.txt': loadQuestions('easy.txt'),
        'medium.txt': loadQuestions('medium.txt'),
        'hard.txt': loadQuestions('hard.txt')
    }
    
    indices ={ ## To keep track of question number
        'easy.txt':0,
        'medium.txt':0,
        'hard.txt':0
    }
    while asked<total_questions:
        if indices[current_file]<len(questions_bank[current_file]):
            q = questions_bank[current_file][indices[current_file]]
            indices[current_file] +=1 ## Incrementing question number
        else:
            print('No more questions')
            break
        print(q[0])
        print(q[1]) 
        print(q[2])  
        print(q[3])  
        print(q[4])
        ans = input('Answer: ').strip().lower()
        if ans == q[5]:
            print('Correct!')
            total_correct += 1    
            total_marks +=marks[current_file]
            if current_file == 'medium.txt':
                current_file = 'hard.txt'
            elif current_file == 'easy.txt':
                current_file = 'medium.txt' 
            elif current_file == 'hard.txt':
                current_file = 'hard.txt' 
        else:
            print('Wrong!')
            print(f'Correct answer is: {q[5]}')
            total_wrong += 1    
            if current_file == 'medium.txt':
                current_file = 'easy.txt'
            elif current_file == 'easy.txt':
                current_file = 'easy.txt' 
            elif current_file == 'hard.txt':
                current_file = 'medium.txt' 
    
        asked += 1

    with open("result.txt", "a") as f:
        f.write(f"Total Correct: {total_correct}\n")
        f.write(f"Total Wrong: {total_wrong}\n")
        f.write(f"Total Marks: {total_marks}\n")

    print("\n===== Quiz Finished =====")
    print("Results saved in result.txt")     
                                   
## Main Program
if __name__ == '__main__':
    marks = {
        'easy.txt': 5,
        'medium.txt': 10,
        'hard.txt': 20
    }

    runQuiz()