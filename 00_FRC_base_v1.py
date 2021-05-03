
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

# string checker




# *** MAIN ROUTINE***

# Set up dictionaries / lists needed to hold data



# Ask the user if they have used the program before & show instruction if necessary



# Loop to get product details (variable cost)
 # start of loop

# initialise loop so that it runs at least once





# --- End of variable cost ---



# ----- Loop to ask for fixed costs -----




# --- End of fixed cost ---


# Profit goal

# Ask for nearest rounding prefered

# Selling price


# ~~PRINTING~~

# variable cost table displaying each item, price and cost -total


# fixed cost table displaying each item, cost - total


# total cost (adding fixed and variable cost)


# Profit and sales targets

# Pricing