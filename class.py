class Person:
    def __init__(self, name, code_meli):
        self.name = name
        self.code_meli = code_meli

    def check_code_meli(self):
       return self.code_meli.isdigit()
    

    def get_info(self):
        return f"name:{self.name} code_meli:{self.code_meli}"



class Student(Person):

        def __init__(self, name, code_meli, students_code):
            super().__init__(name, code_meli)
            self.students_code = students_code

        def get_info(self):
             return f"{super().get_info} student_code:{self.student_code}"
       


st = Student('abolfazl' , '6558664' , '9802023')

print(st.check_code_meli())
