salary = 10000
def calculateBonus(salary):

    if salary < 10000:
        bonus = salary * 0.05
        salary = salary + bonus
        print("Salary after bonus is:", salary)
    else:
            bonus = salary * 0.10
            salary = salary + bonus
            print("Salary after bonus is:", salary)
calculateBonus(10000)
