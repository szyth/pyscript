#!/usr/bin/python

from collections import Counter

dict1 ={}
for i in range(26):
    dict1[chr(97+i)]=(i+1)

str = list(raw_input("Enter a string: "))
inpDict = dict(Counter(str))

count = 0
for char in str:
    if inpDict[char] == dict1[char]:
        count +=1
    else:
        count = 0
        break

if count:
    print('yes')
else:
    print('no')

#print(dict1)
#print(inpDict)
