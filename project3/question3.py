import heapq

def dijkstra1 (s, n, graph, dist, parents, vertices, paths_count):
    visited = [0] * n

    dist[s - 1] = 0
    paths_count[s - 1] = 1
    heap = []
    heapq.heapify (heap)

    heapq.heappush (heap, (0, s))

    while (len (heap) > 0):
        d,v = heapq.heappop (heap)
        if (visited[v - 1] == 0):
            visited[v - 1] = 1

            for u in vertices[v - 1]:
                if (visited[u - 1] == 0):
                    d2 = d + graph[v - 1][u - 1]

                    if (d2 < dist[u - 1]):
                        dist[u - 1] = d2
                        parents[u - 1] = v
                        paths_count[u - 1] = paths_count[v - 1]

                        heapq.heappush (heap, (d2, u))
                    elif (d2 == dist[u - 1]):
                        paths_count[u - 1] = paths_count[u - 1] + paths_count[v - 1]

def dijkstra2 (s, n, graph, dist, vertices):
    visited = [0] * n

    dist[s - 1] = 0
    heap = []
    heapq.heapify (heap)

    heapq.heappush (heap, (0, s))

    while (len (heap) > 0):
        d,v = heapq.heappop (heap)
        if (visited[v - 1] == 0):
            visited[v - 1] = 1

            for u in vertices[v - 1]:
                if (visited[u - 1] == 0):
                    d2 = d + graph[v - 1][u - 1]
            
                    if (d2 < dist[u - 1]):
                        dist[u - 1] = d2

                        heapq.heappush (heap, (d2, u))

def dijkstra3 (s, n, graph, dist, vertices, paths_count):
    visited = [0] * n

    dist[s - 1] = 0
    paths_count[s - 1] = 1
    heap = []
    heapq.heapify (heap)

    heapq.heappush (heap, (0, s))

    while (len (heap) > 0):
        d,v = heapq.heappop (heap)
        if (visited[v - 1] == 0):
            visited[v - 1] = 1

            for u in vertices[v - 1]:
                if (visited[u - 1] == 0):
                    d2 = d + graph[v - 1][u - 1]

                    if (d2 < dist[u - 1]):
                        dist[u - 1] = d2
                        paths_count[u - 1] = paths_count[v - 1]

                        heapq.heappush (heap, (d2, u))
                    elif (d2 == dist[u - 1]):
                        paths_count[u - 1] = paths_count[u - 1] + paths_count[v - 1]

n,e = str (input ()).split ()
n = int (n)
e = int (e)

m,s,t = str (input ()).split ()
m = int (m)
s = int (s)
t = int (t)

graph = [[float ("inf") for i in range(n)] for j in range(n)]
vertices = [[]] * n

for i in range (e):
    a,b,w = str (input ()).split ()
    a = int (a)
    b = int (b)
    w = int (w)
    
    if (w < graph[a - 1][b - 1]):
        graph[a - 1][b - 1] = w
        graph[b - 1][a - 1] = w
        vertices[a - 1] = vertices[a - 1] + [b]
        vertices[b - 1] = vertices[b - 1] + [a]

dist = [float ("inf")] * n
parents = [0] * n
paths_count = [0] * n

parents[s - 1] = 0

dijkstra1 (s, n, graph, dist, parents, vertices, paths_count)

dist2 = [float ("inf")] * n
paths_count2 = [0] * n

dijkstra3 (t, n, graph, dist2, vertices, paths_count2)


if (dist[t - 1] == float ("inf")):
    print (-1)
else:
    path = [t]
    path2 = []

    node = t

    while (parents[node - 1] != 0):
        path.append (parents[node - 1])
        node = parents[node - 1]
    
    for i in path:
        if (paths_count[i - 1] * paths_count2[i - 1] == paths_count[t - 1]):
            path2.append (i)

    dist = [float ("inf")] * n

    dijkstra2 (m, n, graph, dist, vertices)
    
    min_time = dist[path2[0] - 1]

    for i in range (1, len (path2)):
        if (dist[path2[i] - 1] < min_time):
            min_time = dist[path2[i] - 1]

    if (min_time == float ("inf")):
        min_time = -1

    print (min_time)