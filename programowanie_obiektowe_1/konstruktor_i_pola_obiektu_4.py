import random

# Obiekt może zawierać w sobie inne obiekty
class School():
    def __init__(self, name, students) -> None:
        self.name = name
        self.students = students

class Student():

    # Konstruktor może przyjąć argumenty
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

# Obiekt możemy przekazywać jako argumenty do funkcji
def print_student(student):
    print(f"Student : {student.first_name} {student.last_name}, promoted : {student.promoted}")

def promoted_student(student):
    student.promoted = True

# Funkcja może zwracać obiekty
def creata_school_with_students(school_name):
    numbers_of_students = random.randint(1,20)
    students = []
    for student_number in range(numbers_of_students):
        first_name = f"Student-{student_number}"
        last_name = "Smith"
        students.append(Student(first_name,last_name))
    
    school = School(school_name,students)
    return school

def run_example():
    school = creata_school_with_students("Hogwart")
    print(school)
    for student in school.students:
        print_student(student)

if __name__ == '__main__':
    run_example()