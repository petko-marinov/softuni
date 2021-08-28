# Task 5 - Class
class Class:
    students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        self.students.append(name)
        self.grades.append(grade)

    def get_average_grade(self):
        output_average = sum(self.grades)/len(self.grades)
        return output_average

    def __repr__(self):
        str_students = ", " .join(self.students)
        return f"The students in {self.name}: {str_students}. Average grade: {sum(self.grades)/len(self.grades):.2f}"
