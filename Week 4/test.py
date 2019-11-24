def make_a_matrix(str):
    num_of_row = int(input('Enter number of rows of {} matrix: '.format(str)))
    num_of_col = int(input('Enter number columns of {} matrix: '.format(str)))
    print('\nEnter the values in the matrix in the following format\n')
    print('[ [A1, A2 .... An]\n  [B1, B2 .... Bn]\n  [C1, C2 .... Cn] ]\n')
    chrs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    matrix = []
    for each in range(1,num_of_col+1):
        row = []
        for each2 in range(1,num_of_row+1):
            val = float(input('Enter value of {}{}: '.format(chrs[each-1],each2)))
            row.append(val)
        matrix.append(row)
        row = []
    return matrix

def addMatrices(mat_1,mat_2):
    def add_matrix_elements(test_list1, test_list2):
        res_list = []
        for i in range(0, len(test_list1)):
            res_list.append(test_list1[i] + test_list2[i])

        return res_list
    mat_3 = []
    count = 0
    while len(mat_3) != len(mat_1):
        ele = add_matrix_elements(mat_1[count],mat_2[count])
        mat_3.append(ele)
        count = count + 1

    return mat_3


matrix_A = make_a_matrix('first')
matrix_B = make_a_matrix('second')

if len(matrix_A) == len(matrix_B):
    matrix_Resultant = addMatrices(matrix_A,matrix_B)
    print('\nThe Resltant matrix is:\n')
    for row in matrix_Resultant:
        print(row)
else:
    print('Cannot add matrices with diffrent sizes(or dimensions)')