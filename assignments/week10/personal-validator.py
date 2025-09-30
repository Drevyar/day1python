"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")

# Get user input
name = input("Enter your name: ")
age_str = input("Enter your age: ")
phone = input("Enter your phone number: ")

# Validate name (contains only letters and spaces)
is_name_valid = all(char.isalpha() or char.isspace() for char in name.strip())

# Validate age (between 18 and 65)
is_age_valid = False
age = 0
if age_str.isdigit():
    age = int(age_str)
    if 18 <= age <= 65:
        is_age_valid = True

# Validate phone (exactly 10 digits)
is_phone_valid = phone.isdigit() and len(phone) == 10

# Determine age group
age_group = ""
if is_age_valid:
    if 18 <= age <= 30:
        age_group = "Young Adult (18-30)"
    elif 31 <= age <= 50:
        age_group = "Adult (31-50)"
    else:
        age_group = "Senior Adult (51-65)"

# Print validation results
print("\nValidation Results:")
print("Name: %s" % ("Valid (contains only letters and spaces)" if is_name_valid else "Invalid (contains non-letter characters)"))
print("Age: %s" % ("Valid ({} years old)".format(age) if is_age_valid else "Invalid (must be 18-65)"))
print("Phone: %s" % ("Valid (10-digit number)" if is_phone_valid else "Invalid (must be exactly 10 digits)"))

# Print formatted information if all inputs are valid
if is_name_valid and is_age_valid and is_phone_valid:
    print("\nFormatted Information:")
    print("Name: {}".format(name.upper()))
    print("Age Group: {}".format(age_group))
    print("Phone: +66-{}".format(phone))
