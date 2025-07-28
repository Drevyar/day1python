# Empty tuple
empty_tuple = ()
another_empty_tuple = tuple()

# Tuple with values
coordinates = (10, 20)
rgb_color = (255, 128, 0)
mixed_tuple = (1, "hello", 3.14, True)

# Single element tuple (note the comma!)
single_tuple = (42,)  # Without comma, it's just parentheses around a value
not_a_tuple = (42)    # This is just an integer

# Tuple from list
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

# Tuple from string
char_tuple = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')

print(f"Coordinates: {coordinates}")
print(f"RGB: {rgb_color}")
print(f"Mixed: {mixed_tuple}")
print(f"Single: {single_tuple}, type: {type(single_tuple)}")
print(f"Not tuple: {not_a_tuple}, type: {type(not_a_tuple)}")