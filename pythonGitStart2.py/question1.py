'''
Run a sorting algorithm to sort names of students in a class room.
 Assign each of them a student ID. Record each of their marks.
   Find the average marks of the class. Obtain the highest marks of the class 
   using sorting algorithm. Set a grading system. Grade every student  
   and display a report card.

'''
'''students = ['Dipanshu','Deeksha','Dibya','Mita','Gopal']
students.sort()
studentMark = [345,340,378,278,376]'''

students1 = ['Dipanshu','Deeksha','Dibya','Mita','Gopal']
class student:
    def __init__(candidate,name,standard,marks):
        candidate.name=name
        candidate.standard=standard
        candidate.marks=marks
s01=student("Dipanshu","XII",345)
s02=student("Deeksha","XII",340)
s03=student("Dibya","XII",378)
s04=student("Mita","XII",278)
s05=student("Gopal","XII",376)
