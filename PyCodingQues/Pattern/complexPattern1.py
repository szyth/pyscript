#!/usr/bin/python3

#n=5
#*********
#b*******b
#bb*****bb
#bbb***bbb
#bbbb*bbbb


n = int(input("Enter a no.: "))

star = (2*n)-3
b = 'b'
for i in range(n):
    if i>0:
        print(b,end='')
        print('*'*star,end='')
        print(b,end='')
        b +='b'
        star -=2
    else:
        print('*'*(2*n-1),end='')
    print()
