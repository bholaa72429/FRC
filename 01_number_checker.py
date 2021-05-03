# function goes here

# checks that input is a float or an integer which is more zero.
# Has custom error messages for int/float
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

# MAIN ROUTINE
get_int = num_check("How much do you need?(quantity) ",
                    "Please enter an integer (whole number) which is more than 0\n",
                    int)

get_cost = num_check("How much does it costs? $",
                     "Please enter an number that is more than 0\n",
                     float)

print("You need: {}".format(get_int))
print("It coast: ${} ".format(get_cost))