import sys

if len(sys.argv) == 4:
    first = float(sys.argv[1])
    second = float(sys.argv[3])
    if sys.argv[2] == '+':
        print('{} + {} = {}'.format(first,second, first + second))
    elif sys.argv[2] == '-':
         print('{} - {} = {}'.format(first,second, first - second))