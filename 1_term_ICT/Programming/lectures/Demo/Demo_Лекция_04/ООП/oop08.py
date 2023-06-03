# ассоциация (агрегация или композиция), при которой один класс является полем другого

class Salary:
  def __init__(self,pay):
    self.pay = pay
 
  def getTotal(self):
    return (self.pay*12)

# Пример композиции:
class EmployeeK:
  def __init__(self,pay,bonus):
    self.pay = pay
    self.bonus = bonus
    self.salary = Salary(self.pay)

  def annualSalary(self):
    return "Total: " + str(self.salary.getTotal() + self.bonus)
 

# Пример агрегации:
class EmployeeA():
  def __init__(self, pay, bonus):
    self.pay = pay
    self.bonus = bonus

  def annualSalary(self):
    return "Total: " + str(self.pay.getTotal() + self.bonus)


employee = EmployeeK(100,10)
print(employee.annualSalary())


salary = Salary(100)
employee = EmployeeA(salary,10)
print(employee.annualSalary())
