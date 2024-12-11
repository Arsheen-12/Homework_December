'''a = [1, 2]
b = [1, 2]

print(a == b)  # True (values are the same)
print(a is b)  # False (different memory locations)

# Mutable
list_a = [1, 2, 3]
list_a[0] = 99
print(list_a)  # Output: [99, 2, 3]

# Immutable
tuple_a = (1, 2, 3)
tuple_a[0] = 99  # Raises TypeError
print(tuple_a)'''

'''try:
    x = int("not_a_number")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("This block always executes.")


squares = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]
print(squares)

squares_dict = {x: x ** 2 for x in range(5)} 
print(squares_dict)'''


class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

















