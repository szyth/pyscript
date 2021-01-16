import sys


if len(sys.argv)>2:
    
    def add(*args):
        sum = 0.0
        n = len(sys.argv)
        for i in range(1,n):
            sum+=complex(sys.argv[i])
        return sum
                
    print('The sum is : ' + str(add()))

else:
  print('Please input numbers to add in arguments!')
