print('============= BMI Calculator =============')


while True:
    try:
        kilograms = float(input('Enter your weight :'))
        if kilograms > 0:
            break
        else:
            print("Please try again.")
    except ValueError:
        print("Invalid kilograms")


while True:
    try:
        height = float(input('Enter your height :'))
        if height > 0:
            height = height / 100
            break
        else:
            print("Please try again.")
    except ValueError:
        print("Invalid height") 

bmi = kilograms / (height ** 2)

if bmi >= 30.0:
    print('Obese')
elif bmi >= 25.0:
    print('Overweight')
elif bmi >= 18.5:
    print('Normal weight')
else:
    print('Underweight')


print(f'Your weight : {kilograms:.2f}')
print(f'Yoyr height : {height:.2f}')
print(f'Your Bmi is : {bmi:.2f}')

