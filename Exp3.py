import heapq

# ---------------- Union-Find for Kruskal ----------------

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # Path Compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        # Union by Rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        return True


# ---------------- Kruskal's Algorithm ----------------

def kruskal(n, edges):
    """
    edges: list of (weight, u, v)
    Time Complexity: O(E log E)
    """
    edges = sorted(edges)

    uf = UnionFind(n)
    mst = []
    cost = 0

    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w

            if len(mst) == n - 1:
                break

    return mst, cost


# ---------------- Prim's Algorithm ----------------

def prim(n, adj, start=0):
    """
    adj: adjacency list {u: [(v, weight), ...]}
    Time Complexity: O(E log V)
    """
    INF = float('inf')

    key = [INF] * n
    parent = [-1] * n
    inMST = [False] * n

    key[start] = 0

    pq = [(0, start)]
    mst = []
    cost = 0

    while pq:
        w, u = heapq.heappop(pq)

        if inMST[u]:
            continue

        inMST[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, w))
            cost += w

        for v, wt in adj.get(u, []):
            if not inMST[v] and wt < key[v]:
                key[v] = wt
                parent[v] = u
                heapq.heappush(pq, (wt, v))

    return mst, cost


# ---------------- Graph Definition ----------------

n = 7

edges = [
    (7, 0, 1),
    (5, 0, 3),
    (8, 1, 2),
    (9, 1, 3),
    (7, 1, 4),
    (5, 2, 4),
    (15, 3, 4),
    (6, 3, 5),
    (8, 4, 5),
    (9, 4, 6),
    (11, 5, 6)
]

# Build adjacency list for Prim's Algorithm
adj = {}

for w, u, v in edges:
    adj.setdefault(u, []).append((v, w))
    adj.setdefault(v, []).append((u, w))


# ---------------- Kruskal's Algorithm ----------------

kruskal_mst, kruskal_cost = kruskal(n, edges)

print("Kruskal's Minimum Spanning Tree")
print("-" * 35)

for u, v, w in kruskal_mst:
    print(f"{u} -- {v} : {w}")

print("Total Cost =", kruskal_cost)


# ---------------- Prim's Algorithm ----------------

prim_mst, prim_cost = prim(n, adj, start=0)

print("\nPrim's Minimum Spanning Tree")
print("-" * 35)

for u, v, w in prim_mst:
    print(f"{u} -- {v} : {w}")

print("Total Cost =", prim_cost)