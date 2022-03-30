class Student:
    pass

class Grade:
    pass

class School:
    pass

if __name__ == '__main__':
    student_mikolaj = Student()

    grade_a = Grade()
    grade_b = Grade()

    my_school = School()

    print('-'*100)
    print(student_mikolaj)
    print(grade_a, grade_b)
    print(my_school)

    print('-'*100)
    print(f"type(student_mikolaj) : {type(student_mikolaj)}")
    print(f"type(grade_a) : {type(grade_a)},type(grade_b) : {type(grade_b)} ")
    print(f"type(my_school) : {type(my_school)}")

    print('-'*100)
    all_students = [Student(),Student(),Student(),Student(),Student()]
    print(all_students)
    print(all_students[0])
    print(f"type(all_studens) : {type(all_students)}")

    print('-'*100)
    grades = {
        1: Grade(),
        2: Grade(),
    }
    print(grades)
    print(f"type(grades) : {type(grades)}")