Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
}

def get_neighbou(n):
    return Graph_nodes.get(n, [])

def h(n):
    H_dist = {
        'A': 10, 'B': 8, 'C': 5, 'D': 7,
        'E': 3, 'F': 6, 'G': 5, 'H': 3,
        'I': 1, 'J': 0
    }
    return H_dist[n]

def Astar(start, stop):
    openset = {start}
    closed = set()
    g = {start: 0}
    parent = {start: start}

    while openset:
        n = None
        for v in openset:
            if n is None or g[v] + h(v) < g[n] + h(n):
                n = v

        if n is None:
            print("No path")
            return None

        if n == stop:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start)
            path.reverse()
            print('Path found:', path)
            return path

        for (m, weight) in get_neighbou(n):
            if m not in openset and m not in closed:
                openset.add(m)
                parent[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parent[m] = n
                    if m in closed:
                        closed.remove(m)
                        openset.add(m)

        openset.remove(n)
        closed.add(n)

    print("Path does not exist!")
    return None

# Run the A* algorithm
Astar('A', 'J')
