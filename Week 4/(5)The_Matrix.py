# Code by Infiltrat8r

def table(val, val_2):
    count = 0
    for each in range(val,val_2+1):
        print(each, end=' ')
        count = count + 1
        while count == 5:
            print('')
            count = 0


inp = int(input('Enter first: '))
inp_2 = int(input('Enter first: '))

table(inp,inp_2)