class QuickUnion:
    def __init__(self, n):
        """
        Initialize the QuickUnion structure with n elements.
        Each element starts as its own root.
        """
        self.id = list(range(n))  # Each element is initially its own root.

    def root(self, i):
        """
        Find the root of element i.
        """
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        """
        Check if elements p and q are in the same connected component.
        """
        return self.root(p) == self.root(q)

    def union(self, p, q):
        """
        Connect elements p and q by linking the root of one to the root of the other.
        """
        root_p = self.root(p)
        root_q = self.root(q)
        self.id[root_p] = root_q

    def __repr__(self):
        """
        String representation of the current state of the id array.
        """
        return f"{self.id}"


# Example Usage
if __name__ == "__main__":
    n = 10  # Number of elements
    qu = QuickUnion(n)
    
    print("Initial state:", qu)

    # Perform some unions
    qu.union(3, 8)
    print("After union(3, 8):", qu)

    qu.union(4, 9)
    print("After union(4, 9):", qu)

    qu.union(8, 9)
    print("After union(8, 9):", qu)

    # Check connectivity
    print("Are 3 and 9 connected?", qu.connected(3, 9))  # Should return True
    print("Are 1 and 9 connected?", qu.connected(1, 9))  # Should return False
