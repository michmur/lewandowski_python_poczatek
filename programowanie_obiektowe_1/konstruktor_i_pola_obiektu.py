from tokenize import String


class Student():

    # Konstruktor zostanie wywołany podczas tworzenia obiektu
    def __init__(self) -> None:
        print("Powstaje nowy obiekt!")


if __name__ == '__main__':
    student = Student()