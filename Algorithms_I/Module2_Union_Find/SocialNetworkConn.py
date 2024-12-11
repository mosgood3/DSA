"""
Social network connectivity. Given a social network containing nn members and a log file containing mm timestamps at which times pairs of members formed friendships, design an algorithm to determine the earliest time at which all members are connected (i.e., every member is a friend of a friend of a friend ... of a friend). Assume that the log file is sorted by timestamp and that friendship is an equivalence relation. The running time of your algorithm should be mlog⁡nmlogn or better and use extra space proportional to nn.
"""    

class unionFind:
    def ___init___(self,n):
        """
        Initialize the Union-Find data structure.
        n: Number of elements (0 to n-1).

        """
        self.parent = list(range(n)) #creating parent var which is equal to each component in the list, each element is its own parent
        self.size = [1] * n  #the size of each componenet is the number of elemts in the component, initially 1
        self.components = n #Components is initially equal to n as each element is its own component

    def find(self, p):
        """
        Find the root of element p with path compression.
        p: Element to find the root for.

        """
        if p != self.parent[p]: #if p is not its own parent, it is not the root
            self.parent[p] = self.find(self.parent[p]) #Recursive call, this will call the parent of p until the parent of p is it's own root
        return self.parent[p] #the parent of P will be returned when the condition is met
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            if self.size[rootP] < self.size
        
