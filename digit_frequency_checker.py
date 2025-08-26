## Journey from 'Making it work' to 'Making it right'
while(True):
    num = int(input('Enter a positive number: '))
    while(num <= 0):
        num = int(input('Enter a positive number: '))      
    digit = int(input('Enter single digit: '))
    Turns = 1
    while((digit>9 or digit<0) and Turns != 3):
        digit = int(input('Enter single digit: '))
        Turns += 1           
    if(Turns == 3 and (digit>9 or digit<0)):
        print('It seems you don\'t want to follow the instructions.\nGood Bye!') 
        break
    copy = num
    countDigit = 0     
    while(num != 0):
            a = num % 10
            num = num // 10
            if(a == digit):
                countDigit += 1
    print(f'No. of {digit} in {copy} = {countDigit}')          
    op = input('Press Y if you want to enter another number: ').strip().lower()
    if(op == 'n'):
        print()
        print('Thanks !')
        break        
