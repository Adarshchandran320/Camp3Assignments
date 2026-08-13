
class AcademicDetails:
    def academic(self, roll, course, marks):
        self.roll = roll
        self.course = course
        self.marks = marks


class PersonalDetails:
    def personal(self, name, age):
        self.name = name
        self.age = age


class StudentProfile(AcademicDetails, PersonalDetails):
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll)
        print("Course:", self.course)
        print("Marks:", self.marks)


student = StudentProfile()
student.personal("Anjali", 20)
student.academic(101, "BCA", 92)
student.display()