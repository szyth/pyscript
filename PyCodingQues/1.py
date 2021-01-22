#!/usr/bin/python

#digit list should go upto 'hundred', did upto 'nine' for ease
digit = ['zero','one','two','three','four','five','six','seven','eight','nine']

n = map(int,raw_input("Enter nos. separated by a space: ").split())

count=0

def countVowel(number):
    global count
    for x in range(0,len(number)):
        if number[x]=='a'or number[x]=='e'or number[x]=='i'or number[x]=='o'or number[x]=='u':
            count+=1
    return count

for i in range(len(n)):
    countVowel(digit[n[i]])
print(count)

for i in range(1,len(n)-1):
    countPair = 0
    if n[i]+n[i+1]==count:
        print(n[i],n[i+1])
        countPair +=1

print(digit[countPair])
