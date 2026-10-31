class AgeNotValidError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Age {self.age} is not valid"

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeNotValidError(age)
except AgeNotValidError as e:
    print(e)
