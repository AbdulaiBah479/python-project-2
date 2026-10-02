class person:
    def _init_(self,name,age):
        self.name = name
        self.age = age

    def introduce (self):
        print(f"my name is (self.name) and I am (self.age)")

class student(person):
    def _init_(self,name,age, grade,):
        super(). _init_(name,age)
        self.grade = grade

    def study(self):
        print(f"{self.name} studies and has grade{self.grade}")