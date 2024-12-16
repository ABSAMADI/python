class Person:
    def __init__(self, name, code_meli):
        self.name = name
        self.code_meli = code_meli

    def check_code_meli(self):
       return self.code_meli.isdigit()

class Student(Person):

        def __init__(self, name, code_meli, students_code):
            super().__init__(name, code_meli)
            self.students_code = students_code

st = Student('abolfazl' , '6558664' , '9802023')

print(st.code_meli)
