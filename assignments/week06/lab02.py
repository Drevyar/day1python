def calculate_circle(radius):
    pi = 3.14159
    area = round(pi * radius ** 2, 2)
    circumference = round(2 * pi * radius, 2)
    return {"area": area, "circumference": circumference}

result = calculate_circle(2)
print(result)