def get_employees(people=6):
    for people in people:
        for key, value in people.items():
            print(key, value)


class Employees:

    def __init__(self):
        print("Класс сотрудников")
