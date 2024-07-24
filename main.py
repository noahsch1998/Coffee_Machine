from functions import *

make_coffee = True

while make_coffee:
    # Prompt the user for their order (espresso/latte/cappuccino/off/report)
    coffee = input("Please enter your order (espresso/latte/cappuccino)\n")

    # Turn off the machine
    if coffee == 'off':
        make_coffee = False
        break

    # Display the report of available resources
    elif coffee == 'report':
        show_report()
        continue

    # Check for sufficient resources to complete the order
    elif coffee in MENU:
        ingredients_needed = get_ingredient_list(coffee)
        sufficient_resources = verify_sufficient_resources(coffee, ingredients_needed)
        if not sufficient_resources:
            continue

    else:
        print("Please select a valid command\n")
        continue

    # Process payment for the order
    price = show_price(coffee)
    payment = get_payment()

    # Verify that payment is sufficient and return change
    sufficient_payment = verify_payment(payment, coffee)

    # Make a coffee
    if sufficient_payment:
        resources = pour_coffee(coffee, ingredients_needed)
