def welcome_message(name, course):
    return "Welcome [name] to [course] class!"

name = input('Enter your name:')
course = input('Eter your course')
display = welcome_message(name, course)
print(display)