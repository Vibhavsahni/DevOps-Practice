def days_to_hours(no_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{no_of_days} days have {no_of_days * 24 } Hrs"
    elif conversion_unit == "Hours":
        return f"{no_of_days} days have {no_of_days * 24 } Hrs"
    elif conversion_unit == "minutes":
        return f"{no_of_days} days have {no_of_days * 24 * 60 } Mins"
    elif conversion_unit == "Minutes":
        return f"{no_of_days} days have {no_of_days * 24 * 60 } Mins"
    else:
        return "Looks like you're entering a wrong unit value. " \
               "Input 'hours' or 'minutes' only. Also, make sure you give " \
               "a space after the comma"
def validate_and_execute(days_and_unit_dictionary):

    try:
        user_input_number = days_and_unit_dictionary["days"]
        if user_input_number > 0:
            value_in_hours = days_to_hours(user_input_number, days_and_unit_dictionary["unit"])
            print(value_in_hours)
        elif user_input_number == 0:
                print("There can't be zero days! Please enter a positive integer.")

    except ValueError:
        print("You entered a non-digit or negative value, Kindly enter a positive integer value")
