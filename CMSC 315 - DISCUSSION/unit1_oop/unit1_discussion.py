"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Potion:
    potion = "Potion" # class variable
    def __init__(self, date_brewed, price, quantity): # constructor
        self.date_brewed = date_brewed
        self.price = price
        self.quantity = quantity

    def display_info(self): # display information
        print("Brewed:", self.date_brewed, "Price:", self.price, "Quantity:", self.quantity)


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class SleepPotion(Potion):
    sleep_potion = "Sleep Potion"
    def __init__(self, date_brewed, price, duration, dosage, quantity):
        super().__init__(date_brewed, price, quantity)
        self.duration = duration
        self.dosage = dosage
        self.quantity = quantity

    def drink(self): # new method
        self.quantity -= self.dosage
        if self.quantity > 0:
            print("Amount remaining:", self.quantity)
        else:
            print("The bottle is empty")

    def display_info(self): # overriden display_info method
        print(f"Brewed:", self.date_brewed, "Price:", self.price, "Quantity:", self.quantity, "Length of sleep:", self.duration)


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    sleep_potion1 = SleepPotion("10/19/2026", "13 silver", "3 days", 5, 25)
    sleep_potion2 = SleepPotion("9/30/2026", "4 silver", "1 day", 2, 6)

    print("Through class:", SleepPotion.sleep_potion)
    print("Through object:", sleep_potion1.sleep_potion)

    sleep_potion2.rating = 4 # add a new attribute to sleep_potion2

    print(sleep_potion1.__dict__)
    print(sleep_potion2.__dict__)

    print(SleepPotion.__dict__)

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    sleep_potion3 = SleepPotion("8/24/2026", "8 silver", "8 hours", 3, 30)
    sleep_potion3.seller = {"Seller" : "Cuno"}

    # Creates a shallow copy of sleep_potion3. The original object is referenced in regard to nested data, so the copy
    # is dependent on the original and nested data changes accordingly
    shallow_copy = copy(sleep_potion3)
    # Create a copy of sleep_potion3. As a deep copy, nested items are duplicated and the copy is independent of the original
    deep_copy = deepcopy(sleep_potion3)

    sleep_potion3.seller = {"Seller" : "Carlos"}

    print("Original object:", sleep_potion3)
    print("Shallow copy:", shallow_copy)
    print("Deep copy:", deep_copy)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")

    potion1 = Potion("3/15/2026", "2 gold", 30)
    potion1.display_info()

    print("\nTODO: Create and test your child object")

    sleep_potion4 = SleepPotion("11/1/2025", "1 silver", "1 hour", 2, 12)
    sleep_potion4.display_info()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()