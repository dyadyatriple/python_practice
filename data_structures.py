class Disjoint_set:
    def __init__(self,size):
        self.roots=[i for i in range(size)]

    def find_root(self,x):
        return self.roots[x]

    def union(self,x,y):
        root_x=self.find_root(x)
        root_y=self.find_root(y)
        if root_x!=root_y:
            for vertice in range(len(self.roots)):
                if self.roots[vertice]==root_y:
                    self.roots[vertice]=root_x

    def is_connected(self,x,y):
        return self.find_root(x)==self.find_root(y)

