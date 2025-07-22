# Multiple conditions with logical operators
username = "admin"
password = "12345"
is_active = True

if username == "admin" and password == "12345" and is_active:
    print("Access granted")
elif username == "admin" and password == "12345" and not is_active:
    print("Account is deactivated")
else:
    print("Invalid credentials")

# Using 'or' operator
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's weekend!")
else:
    print("It's a weekday")

# Nested if statements
weather = "sunny"
temperature = 28

if weather == "sunny":
    if temperature > 25:
        print("Perfect day for swimming!")
    elif temperature > 15:
        print("Good day for a walk")
    else:
        print("Sunny but cold")
else:
    print("Not a sunny day")