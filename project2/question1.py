n,m = str (input ()).split ()
n = int (n)
m = int (m)

table = [[0] * m] * n

c1 = [[0 for i in range(m)] for j in range(n)]
c2 = [[0 for i in range(m)] for j in range(n)]

for i in range (n):
    table[i] = str (input ()).split ()
    table[i] = list (map (int, table[i]))

c1[0][0] = table[0][0]
c2[0][0] = table[0][0]

for i in range (1, m):
    c1[0][i] = c1[0][i - 1] + table[0][i]
    c2[0][i] = -1

for i in range (1, n):
    for j in range (m):
        if (i == 1):
            if (j == 0):
                c1[i][j] = c1[i - 1][j] + table[i][j]
                c2[i][m - j - 1] = c1[i - 1][m - j - 1] + table[i][m - j - 1]
            else:
                c1[i][j] = min (c1[i - 1][j], c1[i][j - 1]) + table[i][j]
                c2[i][m - j - 1] = min (c1[i - 1][m - j - 1], c2[i][m - j]) + table[i][m - j - 1]
        else:
            if (j == 0):
                c1[i][j] = min (c1[i - 1][j], c2[i - 1][j]) + table[i][j]
                c2[i][ m - j - 1] = min (c1[i - 1][m - j - 1], c2[i - 1][m - j - 1]) + table[i][m - j - 1]
            else:
                c1[i][j] = min (c1[i - 1][j], c2[i - 1][j], c1[i][j - 1]) + table[i][j]
                c2[i][m - j - 1] = min (c1[i - 1][m - j - 1], c2[i - 1][m - j - 1], c2[i][m - j]) + table[i][m - j - 1]  
     
print (c1[n - 1][m - 1])