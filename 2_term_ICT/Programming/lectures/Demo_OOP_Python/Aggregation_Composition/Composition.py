
"""
Пример композиции
"""
class Salary:
  def __init__(self,pay):
    self.pay = pay
 
  def getTotal(self):
    return (self.pay*12)
 
class Employee:
  def __init__(self,pay,bonus):
    self.pay = pay
    self.bonus = bonus
    self.salary = Salary(self.pay)
 
  def annualSalary(self):
    return "Total: " + str(self.salary.getTotal() + self.bonus)
     

if __name__ == "__main__":
    employee = Employee(100,10)
    print(employee.annualSalary())


