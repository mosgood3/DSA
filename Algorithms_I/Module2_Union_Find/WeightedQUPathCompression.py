class WeightedQuickUnionWithPathCompression:
    def __init__(self, n):
        """
        Initialize the Weighted Quick Union structure with n elements.
        """
        self.id = list(range(n))  # Each element is initially its own root.
        self.size = [1] * n       # Size of each component is initially 1.

    def root(self, i):
        """
        Find the root of element i with path compression.
        """
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]  # Point the current node directly to its grandparent.
            i = self.id[i]
        return i

    def connected(self, p, q):
        """
        Check if elements p and q are in the same connected component.
        """
        return self.root(p) == self.root(q)

    def union(self, p, q):
        """
        Connect elements p and q by linking the root of the smaller tree to the larger tree.
        """
        root_p = self.root(p)
        root_q = self.root(q)

        if root_p != root_q:
            # Attach smaller tree to the larger tree
            if self.size[root_p] < self.size[root_q]:
                self.id[root_p] = root_q
                self.size[root_q] += self.size[root_p]
            else:
                self.id[root_q] = root_p
                self.size[root_p] += self.size[root_q]

    def __repr__(self):
        """
        String representation of the current state of the id and size arrays.
        """
        return f"id: {self.id}, size: {self.size}"


# Example Usage
if __name__ == "__main__":
    n = 10  # Number of elements
    wqu_pc = WeightedQuickUnionWithPathCompression(n)

    print("Initial state:", wqu_pc)

    # Perform some unions
    wqu_pc.union(3, 8)
    print("After union(3, 8):", wqu_pc)

    wqu_pc.union(4, 9)
    print("After union(4, 9):", wqu_pc)

    wqu_pc.union(8, 9)
    print("After union(8, 9):", wqu_pc)

    # Check connectivity
    print("Are 3 and 9 connected?", wqu_pc.connected(3, 9))  # Should return True
    print("Are 1 and 9 connected?", wqu_pc.connected(1, 9))  # Should return False
