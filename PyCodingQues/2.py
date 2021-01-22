#!/usr/bin/python

str = raw_input("Enter Equal-Length-Strings separated by a space: ").split()

wordLen = len(str[0])

for i in range(wordLen):
    for n in range(len(str)):
        print(str[n][i])
    print('\n')
