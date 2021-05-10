import pandas
# Functions goes here

# check that product name is not blank


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

# checks that user has entered yes / no to a question
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        # ask question and put response in lowercase
        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        print("please answer yes / no")

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

# Gets expenses, returns list which has
# The data frame and sub total

def get_expenses(var_fixed):
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

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ",
                              "The component name can't be blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity:",
                                 "The amount must be a whole number", int)
        else:
            quantity = 1

        price = num_check("How much? $", "The price must be <more than 0>", float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # calculate cost of each component by multiplying quantity by the price
    expense_frame['Cost'] = expense_frame['Quantity'] \
                            * expense_frame['Price']

    # Find sub total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollar = ['Price', 'Cost']
    for item in add_dollar:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# *** MAIN ROUTINE***

# Get user input
product_name = not_blank("Product Name:",
                         "The product name can't be blank.")

# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# Get fixed costs
fixed_expenses = get_expenses("fixed")
fixed_frame = fixed_expenses[0]
fixed_sub = fixed_expenses[1]



# Profit goal

# Ask for nearest rounding prefered

# Selling price


# ~~PRINTING~~

# display variable costs
print("~~VARIABLE COST ~~")
print(variable_frame)
print()

print("Variable Costs: ${:.2f}".format(variable_sub))


# display fixed cost
print("~~FIXED COST~~")
print(fixed_frame[['Cost']])
print()

print("Fixed Costs: ${:.2f}".format(fixed_sub))

# total cost (adding fixed and variable cost)


# Profit and sales targets

# Pricing