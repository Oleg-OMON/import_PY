from application import salary
from db import people
from datetime import datetime, date, time


def main():
    salary.calculate_salary()
    people.get_employees()
    print(datetime.today())


if __name__ == '__main__':
    main()
