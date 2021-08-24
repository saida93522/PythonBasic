from dataclasses import dataclass


@dataclass  # automatically generates special methods to classes, including __init__()
class Student:
    # fields
    name: str
    school_id: str
    gpa: float

    def __str__(self):
        return f'Name: {self.name} ID: {self.school_id} GPA: {self.gpa}'


def main():
    # student1
    mathew = Student('Mathew', 'cw7847km', 3.6)
    print(mathew)

    # student2
    ali = Student('Ali', 'Lb4964dl', 4.0)
    print(ali)

    # student2
    mary = Student('Mary', 'Sa5664gl', 3.9)
    print(mary)


main()
