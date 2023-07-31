from application.db.people import Employees
from application.salary import salary
from datetime import datetime


if __name__ == '__main__':
    date = datetime.now()
    print(date)
    ivan = Employees()
    get_employees()
    manager2 = salary()
    manager2.calculate_salary('manager')
