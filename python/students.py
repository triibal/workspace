#!/usr/bin/env python

# create student class

class Student(object):
    def __init__(self, name ="", school = "", grade = ""):
        if not name:
            name = raw_input("What is the student's name? ")
        if not school:
            school = raw_input("What is the student's school? ")
        if not grade:
            grade = self.get_grade()
        self.name = name
        self.school = school
        self.grade = grade
        self.print_student()

# create function to input and get grade value to student object

    def get_grade(self):
        while True:
            grade = raw_input("What is the student's grade? [K, 1 - 12] ")
            if grade.lower() not in ['k','1','2','3','4','5','6','7','8','9','10','11','12']
                print " {} isn't valid".format(grade)
            else:
                return grade

# function that prints student object values

    def print_student(self):
        print "Name: {}".format(self.name)
        print "School: {}".format(self.school)
        print "Grade: {}".format(self.grade)


def print_roster(students):
    print "Students in the program:"
    for student in students:
        print "8"*15
        student.print_student()

def main():
    student1 = Student(name = "David", school = "Cranbrook", grade = "11")
    student2 = Student(name = "Byron", school = "Willoughby", grade = "12")
    student3 = Student(name = "Nick", school ="North Sydney", grade = "11")
    students = [student1, student2, student3]
    print_roster(students)
# call main function, will create student1 and student2 and print info

if __name__ == "__main__"
    main()
