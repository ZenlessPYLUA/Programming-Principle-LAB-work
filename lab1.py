def calculate_flooring_cost():
    # user input
    length = float(input("Enter the length of the room in feet"))
    width = float(input("Enter the width of the room in feet"))
    cost_per_square_feet = float(input("Enter the cost of the flooring per square foot: $"))

    # calculate total square feet
    total_square_feet = length * width

    # calculate cost of flooring
    flooring_cost = total_square_feet * cost_per_square_foot

    # calculate tax
    tax_rate = 0.07
    tax_amount = flooring_cost * tax_rate

    # calculate total amount due
    total_amount_due = flooring_cost * tax_amount

    # results
    print("\n---Flooring Cost Summary---")
    print(f"Square Feet needed: {total_square_feet}")
    print(f"Calculate cost of flooring: ${flooring_cost}")
    print(f"Tax amount (7%): ${tax_ammount}")
    print(f"Amount due: ${total_amount_due}")

# run the function
calculate_flooring_cost()
    
