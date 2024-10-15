# Program Name: Lab7.py
# Course: IT1114
# Student Name: Zenzele Broomfield
# Assignment Number: Lab7
# Due Date: 10/13/2024
# Purpose: adding hour and ovetime salaries
# Resources: IDLE(Python 3.12 64 bit)

class Worker:
    def __init__(self):
        self.employee_number = None
        self.office_number = None
        self.first_name = ""
        self.last_name = ""
        self.birthdate = (0, 0, 0) # day month year
        self.hours_worked = 0
        self.overtime_hours_worked = 0
        self.hourly_salary = 0
        self.overtime_salary = 0

    def get_employee_number(self):
        return self.employee_number

    def set_employee_number(self, x):
        self.employee_number = x

    def get_office_number(self):
        return self.office_number
    
    def set_office_number(self, x):
        if 100 <= x <= 500:
            self.office_number = x
            return True
        return False

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
    
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def set_name(self, first, last):
        self.first_name = first
        self.last_name = last

    def get_name(self):
        return self.get_full_name()

    def get_birthdate(self):
        return self.birthdate

    def set_birthdate(self, d, m, y):
        if 1 <= m <= 12 and 1 <= d <= 31:
            self.birthdate = (d, m, y)
            return True
        return False

    def get_hours_worked(self):
        return self.hours_worked
    
    def add_hours(self, x):
        if x > 9:
            self.hours_worked += 9
            self.overtime_hours_worked += x - 9
        else:
            self.hours_worked += x
    def get_hours_overtime(self):
        return self.overtime_hours_worked

    def set_hourly_salary(self, x):
        if x < 0:
            return False
        self.hourly_salary

    def get_hourly_salary(self):
        return self.hourly_salary

    def set_overtime_salary(self, x):
        if x < 0:
            return False
        self.overtime_salary = x
        return True

    def get_overtime_salary(self):
        return self.overtime_salary

    def get_pay(self):
        return (self.hours_worked * self.hourly_salary) + (self.overtime_hours_worked * self.overtime_salary)

    def display_worker_info(self):
        return(f"Employee Number: {self.employee_number}\n"
               f"Office Number: {self.office_number}\n"
               f"Full Name: {self.get_full_name()}\n"
               f"Birthdate: {self.birthdate}\n"
               f"Total Hours Worked: {self.hours_worked}\n"
               f"Total Overtime Hours: {self.overtime_hours_worked}\n"
               f"Total Pay: {self.get_pay()}")

# Script for user input
if __name__ == "__main__":
    worker = Worker()

    # Prompt user for input
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    employee_number = input("Enter employee number: ")
    office_number = int(input("Enter office number (100-500): "))

    # Set user input in the Worker object
    worker.set_first_name(first_name)
    worker.set_last_name(last_name)
    worker.set_employee_number(employee_number)

    # Check if the office number is valid
    if worker.set_office_number(office_number):
        print("Office number set successfully.")
    else:
        print("Invalid office number! Must be between 100 and 500.")

    day = int(input("Enter birth day (1-31): "))
    month = int(input("Enter birth month (1-12): "))
    year = int(input("Enter birth year (e.g., 1990): "))
    
    if worker.set_birthdate(day, month, year):
        print("Birthdate set successfully.")
    else:
        print("Invalid birthdate!")

    # Add hours worked
    hours_worked = int(input("Enter number of hours worked: "))
    worker.add_hours(hours_worked)

    # Set hourly salary and overtime salary
    hourly_salary = float(input("Enter hourly salary: "))
    if worker.set_hourly_salary(hourly_salary):
        print("Hourly salary set successfully.")
    else:
        print("Invalid hourly salary!")

    overtime_salary = float(input("Enter overtime hourly salary: "))
    if worker.set_overtime_salary(overtime_salary):
        print("Overtime hourly salary set successfully.")
    else:
        print("Invalid overtime salary!")

    # Display worker's full info
    print("\nWorker Information:")
    print(worker.display_worker_info())


