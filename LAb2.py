#asking for name of who we are calculating grade for
user_grade = input('Who are we calculating grades for? :\n')

#assiging lab value
user_lab = int(input('Enter the Lab grade: \n'))
if user_lab > 100:
    user_lab = 100
    print('The lab value should have been 100 or less. It has been changed to 100.')
elif user_lab < 0:
    user_lab = 0
    print('The lab value should have been 0 or more. It has been changed to 0.')
else:
    user_lab = user_lab

# assiging EXAM value
user_exam = int(input('Enter the EXAMS grade: \n'))
if user_exam > 100:
    user_exam = 100
    print('The EXAM value should have been 100 or less. It has been changed to 100.')
elif user_exam < 0:
    user_exam = 0
    print('The EXAM value should have been 0 or more. It has been changed to 0.')
else:
   user_exam = user_exam

#assigning attendence value
user_att = int(input('Enter the Attendance grade: \n'))
if user_att > 100:
    user_att = 100
    print('The attendence value should have been 100 or less. It has been changed to 100.')
elif user_att < 0:
    user_att = 0
    print('The attendence value should have been 0 or more. It has been changed to 0.')
else:
    user_att = user_att
#creating space
print()

#creating weighted grade variable
weight_grade = round((user_lab * .7) + (user_exam * .2) + (user_att * .1),1)

if weight_grade >= 90:
    grade_letter = 'A'
elif weight_grade >= 80:
    grade_letter = 'B'
elif weight_grade >= 70:
    grade_letter = 'C'
elif weight_grade >= 60:
    grade_letter = 'D'
else:
    grade_letter = 'F'

#output weighted grade and grade letter, thank you message
print(f'The weighted grade for {user_grade} is {weight_grade}')
print()
print(f'{user_grade} has a letter grade of {grade_letter}')

print()
print('**** Thanks for using the Lab grade calculator ****')

