# Code by Infiltrat8r

# Code by Infiltrat8r


# We will be declaring variables C language style :)

counting_list = ['first', 'second', 'third', 'fourth', 'fifth']  # A list for having some coding magic in inputs.
lis_subjects = []
lis_marks = []
lis_subject_grades = []
total_marks = 0

name = input('Enter your name: ')
father_name = input('Enter your father\'s name: ')
rollnumber = input('Enter your roll number: ')

counter = 0  # The counter for the while loop below.
while counter != 5:  # This loop runs five times and creates a list of subjects and marks.
    subject_input = input('Enter the name of the {} subject: '.format(counting_list[counter]))
    marks_input = int(input('Enter your marks in {} : '.format(subject_input)))
    lis_subjects.append(subject_input)
    lis_marks.append(marks_input)
    counter = counter + 1


def compute_subject_grade(marks):  # Simple function to compute grade
    if marks < 0:
        return 'Inputted marks cannot be graded'
    elif marks < 50:
        return 'Fail'
    elif 50 <= marks < 60:
        return 'C'
    elif 60 <= marks < 70:
        return 'B'
    elif 70 <= marks < 80:
        return 'A'
    elif 80 <= marks <= 100:
        return 'A+'
    else:
        return 'Inputted marks cannot be graded'


for sub_marks in lis_marks:  # This for loop creates a list containing the grades of respective subjects
    sub_grade = compute_subject_grade(sub_marks)
    lis_subject_grades.append(sub_grade)

for sub_marks in lis_marks :  # Computing Overall Total Percentage
    total_marks = total_marks + sub_marks
    percentage = ((total_marks/500)*100)

total_grade = compute_subject_grade(int(percentage))

print('\n\n********* Result Card *********\n\n')
print('Student Name: {}\nFather\'s Name: {}\nRoll no: {}'.format(name, father_name, rollnumber))
print('****************************************************')
print('*Name of Subject * Obtained Marks * Obtained Grade *')
counter_2 = 0
while counter_2 != 5:
    print('****************************************************')
    print('*  {:13} *   {:12} *   {:12} *'.format(lis_subjects[counter_2], str(lis_marks[counter_2]), lis_subject_grades[counter_2]))
    counter_2 = counter_2 + 1
print('*************************************************************************')
print('* Total Obtained *   Total Marks  * Obtained Percentage * Obtained Grade*')
print('*************************************************************************')
print('*  {:11}  *  {:14} *   {:17} *    {:9}  *'.format(str(total_marks), '500', str(percentage), total_grade))
print('*************************************************************************')

# Visit my github for a py verison https://github.com/AmanALA/PF