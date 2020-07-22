
"""
Sum of N numbers by while loop
"""


i=1
sum1 = 0
while i<=10:
    sum1 = i+sum1
    print (sum1)
    i = i+1
    
"""
Program to find PrimeNumber.
"""
inum=int(input('Enter a number'))
if inum==0 or inum==1: 
    print("Enter any other number than 0 and 1") 
else:
    for i in range(2,inum): 
        if inum%i==0:
            print(inum, "is not a prime number") 
        break 
    else: 
        print(inum, 'is a prime number')

