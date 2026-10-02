"""class Dog:
    def __init__(self,name, age):

        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age"""




class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade #0-100

    def get_grade(self):
        return self.grade

class course:
    def __init__(self,name, max_students):
        self.name= name
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_age(self):
        value = 0
        for student in self.students:
            value += student.get_grade
        pass
s1 = student("Tom", 19, 98)
s2 = student("Bill", 17, 80)
s3 = student("Joe", 20, 55)


course = course("science", 2)
course.add_students(s1)
course.add_students(s3)
print(course.students[0].name)


