class disjoint:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0]* n
        

    def findp(self,u):
        if self.parent[u]!=u:
            self.parent[u] = self.findp(self.parent[u])
        return self.parent[u]

    def union(self,u,v):
        u_root = self.findp(u)
        v_root = self.findp(v)

        if u_root == v_root:
            return False
        if (self.rank[u_root]<self.rank[v_root]):
            self.parent[u_root] = v_root
        elif (self.rank[u_root]>self.rank[v_root]):
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] +=1
        return True


def kruskals(graph,node):
    ds = disjoint(node)
    mst = []
    wt = 0

    edges.sort(key = lambda x : x[2])

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            wt += weight

    return mst, wt                          

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

num_nodes = 4

mst, cost = kruskals(edges, num_nodes)
print("Edges in MST:", mst)
print("Total cost of MST:", cost)
