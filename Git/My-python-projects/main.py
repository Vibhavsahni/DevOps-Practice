from helper import validate_and_execute

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter the number of days, the unit of time (minutes/hours) \n")
    list_values = (user_input.split(", "))
    convert_hrs_to_int = int(list_values[0])
    print(list_values)
    days_and_unit_dictionary = {"days": convert_hrs_to_int, "unit": list_values[1]}
    validate_and_execute(days_and_unit_dictionary)




