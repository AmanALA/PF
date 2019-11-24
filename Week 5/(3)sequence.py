# Code by Infiltrat8r

def nthTerm():
    fir_term = int(input('Enter First term of the sequence: '))
    com = int(input('Enater Common difference: '))

    keep_program_running = 'y'
    while True:
        term = fir_term + (int(input('Enter the position of nth term in the list: ')) - 1)*com
        print('The nth term of the sequence is:',term)
        if input('Enter y to continue: ') != 'y':
            break

nthTerm()