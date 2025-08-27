n = int(input('Enter the size of square matrix: '))
A = []

for i in range(n):
    r = [] ## to store individual row
    for j in range(n):
        x = eval(input(f'Enter a{i+1}{j+1}: '))
        r.append(x)
    A.append(r) 
    
sumDiag1 = sum(A[p][p] for p in range(n)) ## Generator Expression
sumDiag2 = sum(A[s][n-s-1] for s in range(n)) 
middle = 0

if(n%2 == 1): # for 3x3 or 5x5 matrix   
    middle = A[n//2][n//2] ## Finding common element at intersection of both diagonals
uniqueSum = sumDiag1 + sumDiag2 - middle   
  
print(f'The sum of main diagonal of {n} x {n} matrix is : {sumDiag1}')  
print(f'The sum of secondary diagonal of {n} x {n} matrix is : {sumDiag2}') 
print(f'The total sum of both diagonals (without double-counting) is: {uniqueSum} ')