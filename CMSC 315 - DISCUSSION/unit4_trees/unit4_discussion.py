"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root_node = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        #call the helper method _insert_recursive to insert the value passed
        #the value is compared to that of existing nodes and assigned as the left child
        #of a node if smaller and vice versa
        self.root_node = self._insert_recursive(self.root_node, value)


    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        #if node is null, create a new node
        if node is None:
            return Node(value)
        #if the new value is smaller than the current node, it is assigned to its left child
        elif value < node.value:
            node.left_child = self._insert_recursive(node.left_child, value)
        #if the new value is greater than the current node, it is assigned to its right child
        elif value > node.value:
            node.right_child = self._insert_recursive(node.right_child, value)

        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        #calls helper method _search_recursive to search the tree and returns true
        #if the value is found
        return self._search_recursive(self.root_node, value)

        #BST searches are often more efficient than linear searches as the value searched
        #is compared to existing elements, routing searches to subtrees rather than looking
        #through every node, unlike linear searches which look through every element
        #until the value searched is found

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        #if node is null, return false
        if node is None:
            return False
        #if the specified value matches the current node, returns true
        elif value == node.value:
            return True

        #compare value to left child if smaller than current node
        if value < node.value:
            return self._search_recursive(node.left_child, value)

        #compare value to right child if greater than current node
        if value > node.value:
            return self._search_recursive(node.right_child, value)

        #if none of the above criteria are met, return false
        return False


    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        #create list to store values
        values = []

        #call _inorder_recursive helper method
        self._inorder_recursive(self.root_node, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        #exit if current node is null
        if node is None:
            return

        #smaller nodes (left children) are visited first
        self._inorder_recursive(node.left_child, values)
        #append to values list
        values.append(node.value)
        #larget nodes (right children) are visited later to print nodes
        #in smallest-to-greatest order
        self._inorder_recursive(node.right_child, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    #create an empty BST for organizations
    orgs = BST()
    #list of org designators
    org_designators = [3909, 2452, 3237, 4059, 1548, 1313, 4212]

    #BSTs are more efficient at reducing search space as values are compared to
    #other nodes from higher to lower levels based on their relative values and routed toward
    #specific subtrees, reducing the number of comparisons made

    #add designators to BST using for loop
    for org_designator in org_designators:
        orgs.insert(org_designator)

    print(f"Organizations:", org_designators)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    #call the inorder method to sort designators in smallest to greatest order
    ordered_designators = orgs.inorder()
    print(f"Designators in order:", ordered_designators)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    #searches for existing values using search method
    print(f"\nSeaches for existing values")
    print(f"Search for 3909:", orgs.search(3909))
    print(f"Search for 1548:", orgs.search(1548))

    #searches for values that do not exist
    print(f"\nSearches for non-existing values")
    print(f"Search for 4604:", orgs.search(4604))
    print(f"Search for 3524:", orgs.search(3524))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    #create and search an empty tree
    single_node_tree = BST()
    print(f"\nSearching empty tree for 1234:", single_node_tree.search(1234))

    #add a single node to the tree
    single_node_tree.insert(1234)
    #print tree value
    print(f"Tree with one node:", single_node_tree.inorder())


if __name__ == "__main__":
    main()