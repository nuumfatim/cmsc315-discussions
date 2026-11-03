"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    #the index and value provided are passed to the List insert() method,
    #which adds the value at the specified index within the list. If there
    #were an element at that index (or any elements that followed that index),
    #they are all shifted to the right by one. If the index is too large, the
    #value is appended to the list
    lst.insert(index, value)

def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    #the if statement checks that the index is larger than or equal to 0 and smaller
    # than the list's length. If these conditions are met, the index is valid and the
    #element at that index is removed and returned.
    #index validation and safe deletion are important as they can help avoid exceptions
    #like IndexError and ValueError, as well as deleting the wrong item

    if (index >= 0) and (index < len(lst)):
        return lst.pop(index)
    else:
        return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    #start item at 0 and iterate through the list's elements
    #this is a linear search as it compares each element to the specified value sequentially
    item = 0
    while item < len(lst):
        if value == lst[item]:
            return item

        item += 1

    #-1 is returned if the previous return statement was not executed
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    #creates and prints the original list
    names = ["Luis", "Mina", "Morris"]
    print("Original list:", names)

    #insert an element at index 0, at the beginning of the list
    #existing elements are shifted to the right by one place
    insert_at(names,0, "Rafael")
    print("Current list:", names)

    #insert an element at index 2
    #the element previously at index 2 (Mina) and the elements that follow it are shifted
    insert_at(names, 2, "Soraya")
    print("Current list:", names)

    #insert an element at the end of the list using the list's length
    insert_at(names, len(names),"Gabriel")
    print("Current list:", names)


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    #remove and print the item at the beginning of the list
    print(delete_at(names, 0))
    print(names)

    #remove and print the value at the middle of the list
    print(delete_at(names, 2))
    print(names)

    #remove and print the value at the end of the list
    print(delete_at(names, len(names)-1))
    print(names)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    existing_value = "Soraya"
    missing_value = "Donna"

    #make a variable for search_value's result of the index or -1 if value not found
    result1 = search_value(names, existing_value)
    #if result1 is greater than -1, and therefore found, print its index
    if result1 > -1:
        print(existing_value, "found at index:", result1)
    else:
        print(existing_value, "not among attendees")

    result2 = search_value(names, missing_value)
    if result2 > -1:
        print(missing_value, "found at index:", result2)
    else:
        print(missing_value, "not among attendees")



    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    #attempt to delete an item at index 6
    #"None" should be returned as the index was greater than the list's length
    #and the list is unchanged
    invalid_index = delete_at(names, 6)
    print(invalid_index)

    #search for a value that is not in the list
    #-1 should be returned
    print(search_value(names, "Marcus"))

    #insert a value to an empty list
    #"Yep" should be the list's only element when printed
    empty_list = []
    insert_at(empty_list, 5, "Yep")
    print(empty_list)

    #delete a value from an empty list
    #"None" should be returned as the condition "index < len(lst)" cannot be met
    empty_list = []
    print(delete_at(empty_list, 0))



if __name__ == "__main__":
    main()