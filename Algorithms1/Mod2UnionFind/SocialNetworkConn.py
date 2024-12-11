class UnionFind:
    def __init__(self, n):
        """
        Initialize the Union-Find data structure.
        n: Number of elements (0 to n-1).
        """
        self.parent = list(range(n))  # Initially, each element is its own parent
        self.size = [1] * n           # Size of each component (1 initially)
        self.components = n          # Total number of components

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
            self.components -= 1  # Decrement the number of components

def earliest_time_to_connect(n, logs):
    logs.sort(key=lambda x: x[0])  # Ensure logs are sorted by timestamp
    uf = UnionFind(n)

    for timestamp, p, q in logs:
        # Debugging statements
        if p < 0 or p >= n or q < 0 or q >= n:
            raise ValueError(f"Invalid member index: p={p}, q={q}, n={n}")

        uf.union(p, q)
        if uf.components == 1:
            return timestamp

    return -1


# Example Usage
n = 6  # Number of members
logs = [
    (20190101, 0, 1),
    (20190104, 1, 2),
    (20190107, 2, 3),
    (20190211, 1, 5),
    (20190224, 2, 4),
]

try:
    print(earliest_time_to_connect(n, logs))
except ValueError as e:
    print(f"Error: {e}")
