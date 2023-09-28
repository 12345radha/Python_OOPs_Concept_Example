class Customer:
  def __init__(self,name,gender):
    self.name=name
    self.gender=gender


def greet(customer):
  if customer.gender=="Female":
    print("Hello",customer.name,"ma'am")
  else
  print("Hello",customer.name,"sir")


cust=Customer("Nitish","Male")
greet(cust)
  
