def dfs (node, vertices, visited_list, group_num, e, d, groups, e_groups, d_groups):
    visited_list[node - 1] = 1

    groups[group_num - 1].append (node)
    e_groups[group_num - 1] = e_groups[group_num - 1] + e[node - 1]
    d_groups[group_num - 1] = d_groups[group_num - 1] + d[node - 1]

    for i in range (len (vertices[node - 1])):
        if (visited_list[vertices[node - 1][i] - 1] == 0):
            dfs (vertices[node - 1][i], vertices, visited_list, group_num, e, d, groups, e_groups, d_groups)


n,m,t =  str (input ()).split ()
n = int (n)
m = int (m)
t = int (t)

e = str (input ()).split ()
e = list (map (int, e))

d = str (input ()).split ()
d = list (map (int, d))

vertices = [[]] * n
visited_list = [0] * n
groups = []
e_groups = []
d_groups = []

for i in range (m):
    n1,n2 = str (input ()).split ()
    n1 = int (n1)
    n2 = int (n2)

    vertices[n1 - 1] = vertices[n1 - 1] + [n2]
    vertices[n2 - 1] = vertices[n2 - 1] + [n1]

group_num = 0

for i in range (n):
    if (visited_list[i] == 0):
        group_num = group_num + 1
        groups.append ([])
        e_groups.append (0)
        d_groups.append (0)

        dfs (i + 1, vertices, visited_list, group_num, e, d, groups, e_groups, d_groups)

c = [[0 for i in range(t)] for j in range(group_num)]

for i in range (t):
    c[0][i] = 0

    if (e_groups[0] <= i + 1):
        c[0][i] = d_groups[0]
    else:
        for k in range (len (groups[0])):
            if (e[groups[0][k] - 1] <= i + 1):
                c[0][i] = max (c[0][i], d[groups[0][k] - 1])
    
for i in range (1, group_num):
    for j in range (t):
        c[i][j] = c[i - 1][j]

        if (e_groups[i] < j + 1):
            c[i][j] = max (c[i][j], c[i - 1][j - e_groups[i]] + d_groups[i])
        elif (e_groups[i] == j + 1):
            c[i][j] = max (c[i][j], d_groups[i])
        else:
            for k in range (len (groups[i])):
                if (e[groups[i][k] - 1] < j + 1):
                    c[i][j] = max (c[i][j], c[i - 1][j - e[groups[i][k] - 1]] + d[groups[i][k] - 1])
                elif (e[groups[i][k] - 1] == j + 1):
                    c[i][j] = max (c[i][j], d[groups[i][k] - 1])

print (c[group_num - 1][t - 1])