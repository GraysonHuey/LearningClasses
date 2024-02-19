from EmployeeSystem import Employee, Manager

# Create an instance of a basic employee
emp1 = Employee('John', 'Doe', 50_000)   # Name is John Doe with a salary of $50,000

print(emp1)  # Show all of the employee's data

print('\n') #For console readability purposes

print(f'Salary: {int(emp1)}')  # Casting to an int returns the employee's salary

print('\n')

print(f'Salary before 5% raise: {emp1.salary}')
emp1.apply_raise() # Use the .apply_raise() method to apply the employee's 5% raise to their salary
print(f'Salary after 5% raise: {emp1.salary}')

print('\n')

print(f'Employee\'s Raise Amount/Multiplier before manual change: {emp1.raiseAmt}')
Employee.raiseAmt = 1.15  # Manually sets the raise amount for the employees. 
# Raise amount must not be lower than 1 or the salary will decrease when applying a raise
print(f'Employee\'s Raise Amount/Multiplier after manual change: {emp1.raiseAmt}')

print('\n')

# The manager class inherits several methods and variables from the employee class
mgr1 = Manager('Jane', 'Doe', 75_000, ['John Doe', 'Jacob Smith']) # Manager's name is Jane Doe with a salary of $75,000 and 2 employees to manage

print('\n')

print(mgr1)  # Show all of the manager's data

print('\n')

print(f'Salary: {int(mgr1)}')  # Casting to an int returns the manager's salary

print('\n')

print(f'Salary before 10% raise: {mgr1.salary}')
emp1.apply_raise() # Use the .apply_raise() method to apply the employee's 5% raise to their salary
print(f'Salary after 10% raise: {mgr1.salary}')

print('\n')

print(f'Manager\'s Raise Amount/Multiplier before manual change: {mgr1.raiseAmt}')
Manager.raiseAmt = 1.25  # Manually sets the raise amount for the managers. 
# Raise amount must not be lower than 1 or the salary will decrease when applying a raise
print(f'Manager\'s Raise Amount/Multiplier after manual change: {mgr1.raiseAmt}')

print('\n')

print(mgr1.get_employees('s')) # Print the manager's employees in string form
print(mgr1.get_employees('l')) # Print the manager's employees in list form

print('\n')

print(mgr1.get_employees('s'))
mgr1.add_employee('Ted Lasso') # Add an employee to the manager
print(mgr1.get_employees('s'))

print(mgr1.get_employees('s'))
mgr1.remove_employee('Ted Lasso') # Remove an employee from the manager
print(mgr1.get_employees('s'))

print(mgr1.is_workday(1))  # Check if it is a workday. In this instance, Monday (1) is a workday
