class Student():

    # Konstruktor może przyjąć argumenty
    def __init__(self, first_nane, last_name) -> None:
        self.first_nane = first_nane
        self.last_name = last_name
        self.promoted = False

# Obiekt możemy przekazywać jako argumenty do funkcji
def print_student(student):
    print(f"Student : {student.first_nane} {student.last_name}, promoted : {student.promoted}")

def run_example():
    student = Student(first_nane="Ola", last_name="Nowak")
    print_student(student)

    other_student = Student("Jerzy","Jurkowski")
    print_student(other_student)

if __name__ == '__main__':
    run_example()