import random
count = 0
for i in range(10):
    x =random.randint(1,15)
    y = random.randint(1,15)
    op = random.randint(1,3)
    
    if(op == 1):
        n = eval(input(f"Enter sum {x}+{y}="))
        if(n == x+y):
            print(f"{x} + {y} = {x + y}\nCorrect")
            count += 1
        else:
             print(f"{x} + {y} = {x + y}\nWrong")
                
    elif(op == 2):
        n = eval(input(f"Enter difference {x} - {y} = "))
        
        if(n == (x - y)):
            print(f"{x} - {y} = {x - y}\nCorrect")
            count+=1
            
        else:
             print(f"{x} - {y} = {x - y}\nWrong") 
               
    else:
        n = eval(input(f"Enter Product {x} * {y} ="))
        if(n == x*y):
            print(f"{x} * {y} = {x * y}\nCorrect")
            count += 1
        else:
             print(f"{x} * {y} = {x * y}\nWrong") 
               
print(f"Your answers were correct {count} times!")

