import os
count = 0
while True:
    userInput = input("""
            Press Enter to Search a keyword: 
            Anything else to Exit:
            """)
    if userInput == '':

        keyword = input('Enter search keyword: ')

        print('''PATH                                   MATCHES\n\n''')
        for root,dirs,files in os.walk('.'):
            for file in files:
                path = os.path.join(root, file)
                with open(path, encoding='ISO-8859-1') as currentfile:
                    for line in currentfile:
                        if keyword in line:
                            print('''{}                                     {}'''.format(path, line))
                            count+=1
        print(count,' entries found!')
#       print('Import result in a file? Yes/No (y/n):')
    else:
        print('Program exited successfully: 200')
        break
