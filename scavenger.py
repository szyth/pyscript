import os
count = 0
while True:
    path = input("\nEnter directory path (Blank for Current Dir): ")
    if path == '':
        path = '.'
    keyword = input("\nEnter a Search keyword:")
#    if keyword == '':
#        print('Program exited successfully: 200')
#        break
#    else:
#        keyword = input('Enter search keyword: ')

    print('''PATH                                   MATCHES\n\n''')
    for root,dirs,files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            with open(path, encoding='ISO-8859-1') as currentfile:
                for line in currentfile:
                    if keyword in line:
                        print('''{}                                     {}'''.format(path, line))
                        count+=1
    print(count,' entries found!')
    again = input("\nSearch Again? (y/n): ")
    if again == 'y' or again == 'Y':
        continue
    else:
        break
#       print('Import result in a file? Yes/No (y/n):')

