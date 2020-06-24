from application.salary import calculate_salary as salary
from application.db.people import get_employsees as employsees
from datetime import datetime

day = datetime.now()
print(day)

if __name__ == '__main__':
    salary()
    employsees()

