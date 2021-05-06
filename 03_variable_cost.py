import pandas


# checks that input is a float or an integer which is more zero.
# has custom error messages for int/float
def num_check(question, error, num_type):
    valid = False

    while not valid:

        try:
            response = num_type(input(question))

            # if response is less or = to 0
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# checks that input is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        # if name is not blank, program continues
        if response != "":
            return response
        # if name is blank, show error message
        else:
            print(error_message)

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Main Routine

# set up dictionaries and lists

# item name list
item_list = []
# item quantity list
quantity_list = []
# item price list
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}
# Get user input
product_name = not_blank("Product Name:",
                         "The product name can't be blank.")

# loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx":

    print()
    # get name, quantity and item
    item_name = not_blank("Item name: ",
                          "The component name can't be blank.")
    if item_name.lower() == "xxx":
        break

    quantity = num_check("Quantity:",
                         "The amount must be a whole number more than zero",
                         int)
    price = num_check("What is the cost for single item? $",
                      "The price must be a number <more than 0>",
                      float)