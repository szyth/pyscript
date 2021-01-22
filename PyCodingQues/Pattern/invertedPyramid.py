#!/usr/bin/python3

#1 1 1 1 1 
#2 2 2 2 
#3 3 3 
#4 4 
#5 


n=int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(i, end=' ')
    print()

