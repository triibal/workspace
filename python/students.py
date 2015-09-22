#!/usr/bin/env python
class Student(object):
    def __init__(self, name ="None", grade = "K", council = "Killara"):
        self.name = name
        self.grade = grade
        self.council = council

student1 = Student()
print student1.name
student2 = Student(name = "Byron", grade = "12", council="Willoughby")
print student2.name
