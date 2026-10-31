class InvalidSalaryError(Exception):
    pass

try:
    salary = int(input("Enter salary amount: "))
    if not 2000 < salary < 5000:
        raise InvalidSalaryError("Salary must be between 2000 and 5000")
except InvalidSalaryError as e:
    print(e)
