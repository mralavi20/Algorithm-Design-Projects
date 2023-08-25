import math

n = int (input ())
m = int (input ())

edges = []
vertices = [0] * n
sources = []

for i in range (m):
    u,v,w = str (input ()).split ()
    u = int (u)
    v = int (v)
    w = float (w)

    w = -(math.log (w))
    
    edges.append ([u, v, w])

    if (vertices[u - 1] == 0 and vertices[v - 1] == 0):
        sources.append (u)
        sources.append (v)
    
    vertices[u - 1] = 1
    vertices[v - 1] = 1

sources.append (n)

status = 0

for i in range (len (sources)):
    dist = [float ("inf")] * n

    dist[sources[i] - 1] = 0

    for j in range (n - 1):
        for k in range (m):
            if (dist[edges[k][0]] != float ("inf")):
                if (dist[edges[k][0]] + edges[k][2] < dist[edges[k][1]]):
                    dist[edges[k][1]] = dist[edges[k][0]] + edges[k][2]

    for j in range (m):
        if (dist[edges[j][0]] != float ("inf")):
            if (dist[edges[j][0]] + edges[j][2] < dist[edges[j][1]]):
                status = 1
                break
    
    if (status == 1):
        break

if (status == 1):
    print ("YES")
else:
    print ("NO")