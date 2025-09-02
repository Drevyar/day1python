def create_user_profile(username, age=18, premium=False):

    if premium:
        status = 'Premium User'
    else:
        status = "Standard User"
    return f"{username} (age: {age}) - {status}"

print(create_user_profile("Bob", 25))
print(create_user_profile("Charlie", 30, True))