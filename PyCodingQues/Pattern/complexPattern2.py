#!/usr/bin/python

#n=10
#**********
#****bb****
#***bbbb***
#**bbbbbb**
#*bbbbbbbb*
#*bbbbbbbb*
#**bbbbbb**
#***bbbb***
#****bb****
#**********

n = int(raw_input("Enter a no.: "))
star = (n/2)-1
b = 'bb'
for i in range(1,n+1):
    if i>1 and i<n:
        if i<=(n/2-1):
            print('*'*star+b+'*'*star)
            star -=1
            b +='bb'
        if i==n/2:
            print('*'*star+b+'*'*star)
            
        if i>=(n/2+1):
            print('*'*star+b+'*'*star)
            star +=1
            b=b[:-2]
    else:
        print('*'*n)


