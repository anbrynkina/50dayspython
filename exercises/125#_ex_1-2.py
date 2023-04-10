# create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter
liters = input("Enter liters you want to convert to cubic meters: ")


def convert_liters_to_cubic_meter(liters):
    cubic_meter = 1000 / float(liters)
    return round(cubic_meter, 2)


print(convert_liters_to_cubic_meter(liters))


# create a script that asks the user to enter a password. then create a func that checks the strength

user_password = input("Enter new password: ")

def strength(password):

    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    uppercase = False

    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


print(strength(user_password))

