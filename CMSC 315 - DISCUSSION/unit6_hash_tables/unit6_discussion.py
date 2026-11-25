"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # create an empty dictionary, stock, and add five items
    stock = {}
    stock["ABCD1234"] = 50
    stock["ABCD1200"] = 80
    stock["EFG36912"] = 25
    stock["EFG51015"] = 1
    stock["HIJ246810"] = 300

    print("Stock items:", stock)


    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    #return the value stored at the provided key
    print("ABCD1234 currently in stock:", stock["ABCD1234"])
    print("EFG36912 currently in stock:", stock["EFG36912"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    #prior to update
    print("Original inventory:\n", stock)

    #assigning a new value to the key, HIJ246810, which replaces the value previously
    #stored at that key
    stock["HIJ246810"] = 298

    #after update
    print("Updated inventory:\n", stock)


    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    #prior to removal
    print("Original inventory:\n", stock)

    #remove a key-value pair
    #this removes EFG51015 and the corresponding stored value, 1, from the dictionary
    del stock["EFG51015"]

    #after removal
    print("Updated inventory:\n", stock)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    #get returns the value for the specified key
    #since the key does not exist, it returns None
    print("Attempting to search for a nonexistent key:", stock.get("XYZ1234"))

    #pop removes the value at the specified key
    #providing a default value (None below) avoids an error
    #since the key provided does not exist, the default value is returned
    print("Deleting a nonexistent key:", stock.pop("LMNO134679", None))

if __name__ == "__main__":
    main()