n = int (input ())

g = []
s = []

for i in range (n):
    temp = []
    temp = str (input ()).split ()
    temp = list (map (int, temp))
    g.append (temp)

m = int (input ())

for i in range (m):
    f,r,u = str (input ()).split ()

    s.append ([int (f), int (r), int (u)])

for k in range (n):
    for i in range (n):
        for j in range (n):
            g[i][j] = min (g[i][j], g[i][k] + g[k][j])

for i in range (m):
    f = s[i][0]
    r = s[i][1]
    u = s[i][2]
    d1 = g[f][r] + g[r][u]
    d2 = g[f][u]

    if (d2 < d1):
        print (d1, d1 - d2)
    else:
        print (d1, 0)