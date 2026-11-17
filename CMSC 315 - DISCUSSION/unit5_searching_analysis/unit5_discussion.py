"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    #iterate through lst's elements using a for loop
    #range begins at 0 and stops at the list's last element
    for x in range(len(lst)):
        #compare the element at index x to target
        if lst[x] == target:
            #return the element's index if it matches the target
            return x
    #if the target is not found, return -1
    return -1

    #linear search usually has a 0(n) time complexity in which n is the size of the
    #list/object searched as it performs the same comparisons sequentially as it iterates
    # through the elements of that object until the target value is found.
    # The best case for a linear search is thus O(1), which occurs when the queried value
    # is the object's first element.


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    low = 0
    high = len(lst) - 1

    while high >= low:
        #find the middle index of the current list/sublist
        mid = (high + low) // 2
        #check whether the score at the mid index is smaller than the target
        if lst[mid] < target:
            #if so, set the low index to mid + 1 and search right sublist
            low = mid + 1
        #check whether the score at the mid index is greater than the target
        elif lst[mid] > target:
            #if so, set high index to mid - 1 and search left sublist
            high = mid - 1
        #these steps eliminate the rest of the list, narrowing the elements left to search

        #if the value stored at the mid index was not smaller or greater than the target score,
        #then the target has been found and its index is returned
        else:
            return mid

    #if a match were not found and the while loop is exited, return -1
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    test_list = [14, 21, 42, 75, 62, 89, 93]

    print("\nExisting value:")
    #both should return 3 as 75's index
    print("Searching for 75 using linear search:", linear_search(test_list,75))
    print("Searching for 75 using binary search:", binary_search(test_list,75))

    print("\nNon-existent value:")
    #both should return -1 as the target value is not in the list
    print("Searching for 100 using linear search:", linear_search(test_list, 100))
    print("Searching for 100 using binary search:", linear_search(test_list, 100))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    #generate a large list of numbers from 1 to 1,000,000
    test_list_large = list(range(1, 1_000_000 + 1))

    #both searches should return 50,999
    print("\nSearching for 51,000 using linear search:", linear_search(test_list_large, 51000))
    print("Searching for 51,000 using binary search:", binary_search(test_list_large, 51000))

    #binary searches are more efficient as datasets grow larger as they iteratively eliminate
    #about half of list as they search for the target value. Linear searches, however, iterate
    #through every element sequentially, becoming inefficient when applied to large datasets


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    test_list_empty = []
    test_list_single = [32]

    #-1 should be returned by both methods
    #as the list is empty, the for loop in the linear search method is skipped and -1 is returned
    print("\nSearching an empty list using linear search:", linear_search(test_list_empty, 54))
    #similarly, as the list's length is 0, high is not larger or equal to low, and the while loop
    #is skipped, returning -1
    print("Using binary search:", binary_search(test_list_empty, 54))

    #0 should be returned by both search methods
    #both methods only need to check one element, in this case, the linear search has a time
    #complexity of O(1)
    print("\nSearching a single-element list using linear search:", linear_search(test_list_single, 32))
    print("Using binary search:", binary_search(test_list_single, 32))

if __name__ == "__main__":
    main()