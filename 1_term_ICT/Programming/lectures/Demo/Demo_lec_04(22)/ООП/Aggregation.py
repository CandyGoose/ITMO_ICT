
"""
Пример агрегации
"""
class Salary():
  def __init__(self, pay):
    self.pay = pay
 
  def getTotal(self):
    return (self.pay * 12)
 
class Employee():
  def __init__(self, pay, bonus):
    self.pay = pay
    self.bonus = bonus
 
  def annualSalary(self):
    return "Total: " + str(self.pay.getTotal() + self.bonus)

     

if __name__ == "__main__":
    salary = Salary(100)
    employee = Employee(salary, 10)
    print(employee.annualSalary())


