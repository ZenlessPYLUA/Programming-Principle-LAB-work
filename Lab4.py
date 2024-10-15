# Program Name: Lab3.py
# Course: IT1114
# Student Name: Zenzele Broomfield
# Assignment Number: Lab2
# Due Date: 9/17/2024
# Purpose: Getting the cost of a resort vacation
# Resources: IDLE(Python 3.12 64 bit)

# function to calculate the room cost
def roomCost(nights, room_selection):
    room_rates = {
        1: 375, # two queen beds
        2: 350, # one king bed
        3: 525, # queen suite
        4: 475, # king suite
    }
    return nights * room_rates[room_selection]

# function to calculate meal cost
def mealCost(brunches, dinners, num_people):
    brunch_cost_per_person = 25
    dinner_cost_per_person = 75
    # total cost per person
    total_brunch_cost = brunches * brunch_cost_per_person
    total_dinner_cost = dinners * dinner_cost_per_person
    # total for all
    total_meal_cost = total_brunch_cost + total_dinner_cost
    return total_meal_cost

# function to calculate excursion cost
def excursionCost(picnic, snorkeling, guided_hike, boat_dinner, num_people):
    picnic_cost = 50 if picnic else 0
    snorkeling_cost = 25 * num_people if snorkeling else 0
    hike_cost = 17 * num_people if guided_hike else 0
    boat_dinner_cost = 200 if boat_dinner else 0
    return picnic_cost + snorkeling_cost + hike_cost + boat_dinner_cost

# main function for getting the total vacation cost
def main():
    # room selection and number of nights
    nights = int(input("Number of nights: "))
    num_people = int(input("Number of people: "))

    print("Room Types:\n(1) - Two Queen Beds\n(2) - One King Bed\n(3) - Queen Suite\n(4) - King Suite")
    room_selection = int(input("Select Type (1-4): "))

    # meal options
    brunches = int(input("How many Brunches: "))
    dinners = int(input("How many Dinners: "))

    # excursion options
    picnic = input("Picnic? (y/n): ").lower()=='y'
    snorkeling = input("Snorkeling? (y/n): ").lower()=='y'
    guided_hike = input("Guided Hike? (y/n): ").lower()=='y'
    boat_dinner = input("Boat Dinner? (y/n): ").lower()=='y'

    # calculating the cost
    room_cost = roomCost(nights, room_selection)
    meal_cost = mealCost(brunches, dinners, num_people)
    excursion_cost = excursionCost(picnic, snorkeling, guided_hike, boat_dinner, num_people)

    # gratuity
    gratuity = meal_cost * 0.15
    total_meal_cost_with_gratuity = meal_cost + gratuity

    # cost display
    print(f"Room Cost: ${room_cost}")
    print(f"Meal Cost: ${total_meal_cost_with_gratuity}")
    print(f"Excursion Cost: ${excursion_cost}")

    # total cost
    total_cost = room_cost + total_meal_cost_with_gratuity + excursion_cost
    print(f"Total Cost: ${total_cost}")

# run
if __name__ == "__main__":
    main()
