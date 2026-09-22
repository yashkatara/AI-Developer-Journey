class Programmer: 
  company = "Microsoft"
  def __init__(self, name, salary, pin  ):
    self.name = name
    self.salary = salary
    self.pin = pin  
    
p = Programmer("Yash", 100000, 1234)
print(p.company,p.name,p.salary,p.pin)    