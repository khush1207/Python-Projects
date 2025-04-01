# Coffee Machine Program
# This program simulates a simple coffee machine that takes orders, processes payments, and dispenses coffee.

# Menu with drink ingredients and their costs
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}

# Available resources in the coffee machine
resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0.0}


# Function to print a report of available resources
def print_report():
    print("\nMachine Resources Report:")
    for key, value in resources.items():
        unit = "ml" if key in ["water", "milk"] else "g" if key == "coffee" else "$"
        print(f"{key.capitalize()}: {value}{unit}")
    print()


# Function to check if there are enough resources to make a drink
def check_resources(drink):
    for item, amount in MENU[drink]["ingredients"].items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item} to make {drink}.")
            return False
    return True


# Function to process coin input and return total amount inserted
def process_coins():
    print("\nPlease insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return round(total, 2)


# Function to check if the transaction is successful
def transaction_successful(payment, drink):
    cost = MENU[drink]["cost"]
    if payment < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    resources["money"] += cost  # Add the money to the machine's resources
    if payment > cost:
        print(f"Here is ${round(payment - cost, 2)} in change.")
    return True


# Function to make the coffee by reducing used ingredients
def make_coffee(drink):
    for item, amount in MENU[drink]["ingredients"].items():
        resources[item] -= amount
    print(f"Enjoy your {drink}! ☕\n")


# Main coffee machine function
def coffee_machine():
    while True:
        choice = input(
            "\nWhat would you like? (espresso/latte/cappuccino) or 'report' to check resources, 'off' to exit: ").lower()

        if choice == "off":
            print("Turning off the coffee machine. Have a great day! ☕")
            break
        elif choice == "report":
            print_report()
        elif choice in MENU:
            if check_resources(choice):
                payment = process_coins()
                if transaction_successful(payment, choice):
                    make_coffee(choice)
        else:
            print("Invalid selection. Please choose a valid option.")


# Run the coffee machine program
coffee_machine()
