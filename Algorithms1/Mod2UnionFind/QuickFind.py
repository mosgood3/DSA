

class Quickfind:
    def __init__(self,n):
        self.id = list(range(n))
    def connected(self, p, q):
        return self.id[p] == self.id[q]
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid

    def __repr__(self):
        return f"{self.id}"
    
if __name__ == "__main__":
    n = 10  # Number of elements
    qf = Quickfind(n)

    print("Initial state:", qf)

    # Perform some unions
    qf.union(3, 8)
    print("After union(3, 8):", qf)

    qf.union(4, 9)
    print("After union(4, 9):", qf)

    qf.union(8, 9)
    print("After union(8, 9):", qf)

    # Check connectivity
    print("Are 3 and 9 connected?", qf.connected(3, 9))
    print("Are 1 and 9 connected?", qf.connected(1, 9))
