"""
Question 2

Union-find with specific canonical element. Add a method find()find() to the union-find data type so that find(i)find(i) returns the largest element in the connected component containing ii. The operations, union()union(), connected()connected(), and find()find() should all take logarithmic time or better.

For example, if one of the connected components is {1,2,6,9}, then the find()find() method should return 99 for each of the four elements in the connected components.

"""


class UnionFind:
    def __init__(self, n):
        """
        Initialize the Union-Find data structure.
        n: Number of elements (0 to n-1).
        """
        self.parent = list(range(n))  # Initially, each element is its own parent
        self.size = [1] * n           # Size of each component (1 initially)
        self.components = n
        self.largest = list(range(n))    

    def find(self, p):
        """
        Find the root of element p with path compression.
        p: Element to find the root for.
        """
        if p != self.parent[p]:  # If p is not its own parent, recursively find the root
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]
    
    def union(self, p, q):
        """
        Merge the components containing p and q.
        """
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:  # Only merge if they are in different components
            # Attach smaller tree to larger tree
            if self.size[rootP] < self.size[rootQ]:
                rootP, rootQ = rootQ, rootP
            self.parent[rootQ] = rootP  # Make rootP the parent of rootQ
            self.size[rootP] += self.size[rootQ]  # Update the size of the new tree
            self.largest[rootP] = max(self.parent[rootP], self.parent[rootQ])
            self.components -= 1  # Decrement the number of components

    def connected(self, p , q):
        return self.parent(p) == self.parent(q)
    
    def findlargest (self, p):
        rootP = self.find(p)
        return self.largest[rootP]
    

    # Example usage
uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 6)
uf.union(3, 4)
uf.union(4, 5)
print(uf.findlargest(1))  # Output: 6 (largest in the component containing 1, 2, 6)
print(uf.findlargest(3))  # Output: 5 (largest in the component containing 3, 4, 5)
print(uf.connected(1, 6))  # Output: True (1 and 6 are connected)
print(uf.connected(1, 3))  # Output: False (1 and 3 are not connected)
