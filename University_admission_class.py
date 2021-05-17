class Student:
    def __init__(self):
        self.__student_id = None
        self.__age = None
        self.__marks = None
        self.__course_id = None
        self.__fees = None

    def set_student_id(self, student_id):
        self.__student_id = student_id
    def set_age(self, age):
        self.__age = age
    def set_marks(self, marks):
        self.__marks = marks

    def get_student_id(self):
        return self.__student_id
    def get_age(self):
        return self.__age
    def get_marks(self):
        return self.__marks
    def get_course_id(self):
        return self.__course_id
    def get_fees(self):
        return self.__fees

    def validate_marks(self):
        return self.__marks >= 0 and self.__marks <= 100

    def validate_age(self):
        return self.__age > 20

    def check_qualification(self):
        return self.validate_marks() and self.validate_age() and self.__marks >= 65

    def choose_course(self, course_id):
        if self.check_qualification() and (course_id == 1001 or course_id == 1002):
            self.__course_id == course_id
            if self.__course_id == 1001:
                self.__fees == 25575
            elif self.__course_id == 1002:
                self.__fees = 15500
            if self.__marks > 85:
                self.__fees = self.__fees/(self.__fees*25/100)
            return True
        else:
            return False

maddy=Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(65)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")
