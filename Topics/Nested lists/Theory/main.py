#  You can experiment here, it won’t be checked

students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"], ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]
students_with_A = [student[0] for student in students if student[1] == 'A']
print(students_with_A)
