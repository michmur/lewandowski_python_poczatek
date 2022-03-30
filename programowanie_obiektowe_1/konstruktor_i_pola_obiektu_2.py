class Student():

    # Zadaniem konstruktora jest zdefiniować i zainicjować stan obiketu
    def __init__(self) -> None:
        self.first_nane = "Mikołaj"
        self.last_name = "Lewandowski"
        self.age = 54


def run_example():
    student = Student()
    # Do stanu obiektu mamy dostęp - możemy go odczytać
    print(f"imie : {student.first_nane}, nazwisko : {student.last_name} wiek : {student.age}")
    
    # Stan obiektu możemy również zmodyfikować
    student.first_nane = "Jakub"
    student.last_name = "Kowalski"
    student.age = 30
    print(f"imie : {student.first_nane}, nazwisko : {student.last_name} wiek : {student.age}")

if __name__ == '__main__':
    run_example()