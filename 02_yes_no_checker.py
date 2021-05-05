# yes/no function goes here

def yes_no(question):

    to_check = ["yes","no"]

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

# Main routine
for item in range (0,6):
    want_help = yes_no("Do you want to read instructions ? ")
    print("You said ")