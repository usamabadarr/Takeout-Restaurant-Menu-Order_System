def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices, using the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    # Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order = []

    # Get the menu items mapped to the menu numbers
    menu_items = get_menu_items_dict(menu)

    # Launch the store and present a greeting to the customer
    print("Welcome to the Generic Take Out Restaurant.")

    place_order = True
    # TODO: Create a continuous while loop so customers can order multiple items
    while place_order:
        # TODO: Loop through the menu dictionary, extracting the food category and
        # the options for each category
        for food_category, options in menu.items():
            # TODO: Loop through the options for each food category, extracting the
            # meal and the price
            for meal, price in options.items():
                # TODO: Print the menu item number, food category, meal, and price
                print(f"{meal} - {food_category} - ${price}")
                # TODO: Update the menu selection number
                # (This part can be handled in the input loop below)

        # Ask customer to input menu item number
        menu_selection = input("Type menu number: ")

        # Update the order list using the update_order function
        # Send the order list, menu selection, and menu items as arguments
        order = update_order(order, menu_selection, menu_items)

        # Ask the customer if they would like to order anything else
        # Let the customer know if they should type 'n' or 'N' to quit
        keep_ordering = input("Would you like to keep ordering? (N) to quit: ")

        # TODO: Write a conditional statement that checks if the customer types
        # 'n' or 'N'
        if keep_ordering.lower() == 'n':
            # Since the customer decided to stop ordering, thank them for
            # their order
            print("Thank you for your order.")

            # TODO: Use a list comprehension to create a list called prices_list,
            # which contains the total prices for each item in the order list:
            # The total price for each item should multiply the price by quantity
            prices_list = [item['Price'] * item['Quantity'] for item in order]

            # TODO: Create an order_total from the prices list using sum()
            # and round the prices to 2 decimal places.
            order_total = round(sum(prices_list), 2)

            # Write a break statement or set the condition to False to exit
            # the ordering loop
            place_order = False

    # TODO: Return the order list and the order total
    return order, order_total


def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered (updated as needed).
    """
    # TODO: Check if the customer's input string can be converted 
    # to an integer and prints an error message if it does not
    try:
        menu_selection = int(menu_selection)
    except ValueError:
        print("Invalid selection. Please enter a number.")
        return order

    # TODO: Write a conditional statement that checks if the customer's input is 
    # an item on the menu and prints an error message if it is not
    if menu_selection not in menu_items:
        print("Invalid menu selection. Please choose a valid item.")
        return order

    # Store the item name as a variable
    item_name = menu_items[menu_selection]["Item name"]

    # TODO: A prompt (input) to the customer that prints the name of the 
    # menu item to the user and asks the quantity they would like to order.
    # Store the return in a quantity variable
    quantity = input(f"How many {item_name} would you like to order? ")

    # TODO: Write a conditional statement that checks if the input quantity 
    # can be converted to an integer, then converts it to an integer. 
    # Have it default to 1 if it does not.
    try:
        quantity = int(quantity)
    except ValueError:
        print("Invalid quantity. Defaulting to 1.")
        quantity = 1

    # TODO: Add a dictionary with the item name, price, and quantity to the 
    # order list. Use the following names for the dictionary keys:
    # "Item name", "Price", "Quantity"
    order.append({
        "Item name": item_name,
        "Price": menu_items[menu_selection]["Price"],
        "Quantity": quantity
    })

    # TODO: Return the updated order
    return order


def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
    # Uncomment the following line if you need to check the structure of the receipt
    #print(receipt)

    # TODO: Loop through the items in the customer's receipt
    for item in receipt:
        # TODO: Store the dictionary items ("Item name", "Price", "Quantity") as variables
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]

        # TODO: Print the receipt line using the print_receipt_line function
        # send the item name, price, and quantity as separate arguments
        print_receipt_line(item_name, price, quantity)


##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################


def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")


def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")


def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")


def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")


def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")


def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    menu_items = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the menu_items
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    # Return the completed dictionary of menu items
    return menu_items


def main():
    # Set up menu with categories and items
    menu = {
        "Appetizers": {
            "Spring Roll": 5.99,
            "Dumplings": 6.99,
            "Garlic Bread": 3.99
        },
        "Mains": {
            "Cheeseburger": 12.99,
            "Pizza": 14.99,
            "Pasta": 13.99
        },
        "Drinks": {
            "Soda": 1.99,
            "Water": 0.99,
            "Juice": 2.49
        }
    }

    # TODO: Call the `print_menu_heading` function to print the heading
    print_menu_heading()

    # TODO: Call the `place_order` function to take the order and calculate the total
    order, total_price = place_order(menu)

    # TODO: Call the `print_itemized_receipt` function to display the receipt
    print_itemized_receipt(order)

    # TODO: Call the `print_receipt_footer` function to print the receipt footer
    print_receipt_footer(total_price)

if __name__ == "__main__":
    main()
