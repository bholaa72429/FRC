import pandas
import math
# **Functions goes here**

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

# Prints expense frames
def expense_print(heading, frame, subtotal):
    print()
    print("***{} Costs ***".format(heading))
    print(frame)
    print()
    print(" {} Costs: ${:.2f}".format(heading,subtotal))
    return ""

def profit_goal(total_costs):

    # Initialise variable and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal
        response = input("What is your profit goal (eg $200 or 20%) ? ")

        # check if the first character is $
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # chech that last character is %
        elif response [-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]
        else :
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is an number more than zero
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue
        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}. "
                                 "ie {:.2f} dollar? ,"
                                 "y/n".format(amount, amount))
            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}% , y/n ? ".format(amount))

            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal

# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to




# *** MAIN ROUTINE***
instructions = yes_no("Would you Like to See instructions?")
if instructions != "yes":
    print("Welcome")
else:
    print("use The following guidlines")

# Ask user if they have used the program before & show instruction

# Get user input
product_name = not_blank("Product Name:",
                         "The product name can't be blank.")

how_many = num_check("How many items will you be producing?",
                     "The number of items must be a whole number more than zero",
                     int)


print()
print("Please enter your variable costs below...")
# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have  fixed costs (y/n)? ")

if have_fixed == "yes":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0

# work out the total costs amd profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# calculate total sales needed to reach goal.
sales_needed = all_costs + profit_target

# Ask for nearest rounding prefered
round_to = num_check("Round to nearest ...? $",
                     "can't be 0",int)
# Calculate the recommended price
selling_price = sales_needed / how_many
print("Selling Price (unrounded): ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)


# change frame to string
variable_txt = pandas.DataFrame.to_string(variable_frame)
fixed_txt = pandas.DataFrame.to_string(fixed_frame)

# ~~PRINTING~~

print()
print("^^^ Fund Raising - {} ^^^".format(product_name))
print()
expense_print("Variable", variable_frame, variable_sub)

if have_fixed == "yes":
    expense_print("Fixed", fixed_frame[['Cost']], fixed_sub)

# total cost (adding fixed and variable cost)
print()
print("Total Cost: ${:.2f}".format(all_costs))
print()

print()
print("*** Profit and Sales Targets ***")
print("Profit Target: ${:.2f}".format(profit_target))
print("Total Sales: ${:.2f}".format(all_costs + profit_target))


# Profit and sales targets
print(" *** Pricing ***")
print("Minimum Price: $ {:.2f}".format(selling_price))
print("Recommended Price: ${:.2f}".format(recommended_price))

# Pricing



to_write = [product_name, variable_txt, fixed_txt,
            profit_target, selling_price, recommended_price]

# Write to file ...
# create file to hold data ( add .txt extension)
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# heading
for item in to_write:
    text_file.write(str(item))
    text_file.write("\n\n")


# close your text file
text_file.close()
