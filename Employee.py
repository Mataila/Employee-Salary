class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, 0)  # Base salary not needed for hourly employees
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        self.salary = self.hourly_rate * self.hours_worked
        return self.salary

class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name, monthly_salary)
    
    def calculate_salary(self):
        return self.salary

if __name__ == "__main__":
    hourly_emp = HourlyEmployee(emp_id=1, name="James Kimatu", hourly_rate=20, hours_worked=160)
    salaried_emp = SalariedEmployee(emp_id=2, name="Eric Wambua", monthly_salary=5000)
    
    print(f"Hourly Employee Salary: {hourly_emp.calculate_salary()}")
    print(f"Salaried Employee Salary: {salaried_emp.calculate_salary()}")
