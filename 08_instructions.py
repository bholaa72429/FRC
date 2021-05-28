# Function
def string_check(choice, options):

    is_valid = "yes"
    chosen = ""
    for var_list in options:

        # if the snack  is in one of the lists, return the full
        if choice in var_list:

            # Get full name of snacks abd put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions? ").lower()
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print()
        print("^^^^Fundraising Calculator Instructions^^^^")
        print()
        print("--Welcome to FRC -- ")
        print("This is a platform where you can use to calculate your cost for fundraising event")

    return ""

# ******** Main Routine *******
# lists for valid options for yes / no response
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# Ask If instructions are needed
instructions(yes_no)
print()
print("Program Launches ...")