# Program Name: Lab3.py
# Course: IT1114
# Student Name: Zenzele Broomfield
# Assignment Number: Lab2
# Due Date: 9/8/2024
# Purpose: Getting the total number of sales for the department
# Resources: IDLE(Python 3.12 64 bit)

def department_sales():
    # manager enters the sales goal for the month
    sales_goal = float(input("Sales goal: $"))

    # variables
    total_sales = 0
    total_employees = 0

    # outer loop for multiple salespersons
    while True:
        total_employee_sales = 0
        total_employees += 1

        # inner loop to enter sales for 4 weeks for each person
        for week in range(1, 5):
            weekly_sales = float(input(f"Salesperson {total_employees} week {week} : $"))
            total_employee_sales += weekly_sales

        # total department sales
        total_sales += total_employee_sales

        # if theres another salesperson
        another = input("Another salesperson? (y/n): ").lower()
        if another != 'y':
            break

    # managers bonus based on total sales and sales goal
    if total_sales > sales_goal:
        manager_bonus = total_sales * 0.05
    else:
        manager_bonus = total_sales * 0.02

    # results
    print("Department Monthly Sales and Commission")
    print(f"Number of Employees: {total_employees}")
    print(f"Department Sales Goal: ${sales_goal:.2f}")
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"Mgr. Bonus: ${manager_bonus:.2f}")

department_sales()
