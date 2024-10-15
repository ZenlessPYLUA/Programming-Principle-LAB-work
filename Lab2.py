# Program Name: Lab2.py
# Course: IT1114
# Student Name: Zenzele Broomfield
# Assignment Number: Lab2
# Due Date: 9/1/2024
# Purpose: Get the total amount due for a order of pizzas and salads
# Resources: IDLE(Python 3.12 64 bit)

def calculate_hackathon_food_cost():
    num_pizza_orders = int(input("Enter the number of people who ordered pizza"))
    num_salad_orders = int(input("Enter the number of people who ordered salad"))

    # Constants
    slice_per_person = 3
    slice_per_pizza = 12
    pizza_cost = 15.99
    salad_cost = 7.99
    discount_threshold = 10
    discount_rate = 0.15
    delivery_charge_rate = 0.07
    min_delivery_charge = 20.00

    # Number of pizzas needed
    total_slices_needed = num_pizza_orders * slice_per_person

    # cost before discount
    total_pizza_cost = ((total_slices_needed + slice_per_pizza - 1) // slice_per_pizza) * pizza_cost
    total_salad_cost = num_salad_orders * salad_cost
    total_due = total_salad_cost + total_pizza_cost

    # discounts
    total_discount = ((total_pizza_cost * discount_rate if num_pizza_orders > discount_threshold else 0)+ (total_salad_cost * discount_rate if num_salad_orders > discount_threshold else 0))

    #delivery charge
    initial_total_cost = total_pizza_cost + total_salad_cost
    delivery_charge = max(initial_total_cost * delivery_charge_rate, min_delivery_charge)

    # total amount due
    total_amount_due = initial_total_cost - total_discount + delivery_charge

    # results
    print(f"\nNumber of pizzas ordered: {num_pizza_orders}")
    print(f"Number of salads ordered: {num_salad_orders}")
    print(f"Pizza cost : ${total_pizza_cost:.2f}")
    print(f"Salad cost: ${total_salad_cost:.2f}")
    print(f"Total: ${total_due:.2f}")
    print(f"Discount: -${total_discount:.2f}")
    print(f"Delivery charge: ${delivery_charge:.2f}")
    print(f"Total amount due: ${total_amount_due:.2f}")

calculate_hackathon_food_cost()
