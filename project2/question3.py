n = int (input ())
h = str (input ()).split ()

h = list (map (int, h))

h2 = [*set (h)]
h2.sort ()

count_h = len (h2)

c = [[[0 for i in range (count_h)] for j in range (n)] for k in range (n)]

for i in range (n):
    for j in range (0, h2.index (h[i]) + 1):
        c[i][i][j] = 1

for k in range (count_h - 1, -1, -1):
    for i in range (2, n + 1):
        for j in range (n):
            t = i + j - 1
        
            if (t < n):
                if (h[j] == h[t] and k <= h2.index (h[j])):
                    if (j == t - 1):
                        c[j][t][k] = c[j + 1][t][k] + c[j][t - 1][k] + 1
                    else:
                         c[j][t][k] = c[j + 1][t][k] + c[j][t - 1][k] - c[j + 1][t - 1][k] + c[j + 1][t - 1][h2.index (h[j])] + 1
                else:
                    if (j == t - 1):
                        c[j][t][k] = c[j + 1][t][k] + c[j][t - 1][k]
                    else:
                        c[j][t][k] = c[j + 1][t][k] + c[j][t - 1][k] - c[j + 1][t - 1][k]

print ((c[0][n - 1][0]) % ((10 ** 9) + 7))