from datetime import datetime

class Employee:
    """Employee Class"""
    # Constructor
    def __init__(self, lname, fname, address, phone_number):
        self._last_name = lname
        self._first_name = fname
        self._emp_address = address
        self._emp_phone_number = phone_number



    def set__last_name(self, lname):
        self._last_name = lname

    def set__first_name(self, fname):
        self._first_name = fname

    def set__emp_address(self, address):
        self._emp_address = address

    def set__emp_phone_number(self, phone_number):
        self._emp_phone_number = phone_number


    def display(self):
        return str(self._last_name) + ", " + str(self._first_name) + ", " + str(self._emp_address) + ", " + str(self._emp_phone_number)

class SalariedEmployee(Employee):
    def __init__(self, l, f, a, p, date, salary):
        super().__init__(l, f, a, p)
        self.start_date = date
        self.employee_salary = salary

    def give_raise(self, new_pay):
        if new_pay != self.employee_salary:
            self.employee_salary = new_pay

    def display(self):
        return str(self._last_name) + ", " + str(self._first_name) + ", " + str(self._emp_address) + ", " + str(self._emp_phone_number) + ", " + str(self.start_date) + ", " + str(self.employee_salary)

class HourlyEmployee(Employee):
    def __init__(self, l, f, a, p, date, hourly):
        super().__init__(l, f, a, p)
        self.start_date = date
        self.employee_hourly = hourly

    def give_raise(self, new_pay):
        if new_pay != self.employee_hourly:
            self.employee_hourly = new_pay

    def display(self):
        return str(self._last_name) + ", " + str(self._first_name) + ", " + str(self._emp_address) + ", " + str(self._emp_phone_number) + ", " + str(self.start_date) + ", " + str(self.employee_hourly)


#Driver
salary_employee1 = SalariedEmployee('Essick', 'Nate', '123 Hawkeye St', '123-456-7890', datetime(2020, 11, 9), 30000)
print(salary_employee1.display())
salary_employee1.give_raise(45000)
print(salary_employee1.display())
del(salary_employee1)
hourly_employee1 = HourlyEmployee('Manning', 'Peyton', '18 Quarterback Rd', '181-818-1818', datetime(1998, 4, 18), 8.00)
print(hourly_employee1.display())
hourly_employee1.give_raise(12.00)
print(hourly_employee1.display())
del(hourly_employee1)

