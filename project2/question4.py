def find_min (l_index, r_index, a, c):
    if (l_index > r_index):
        return 0
    if (l_index == r_index):
        return 1
    
    count = r_index - l_index + 1
    min_h = min (a[l_index:r_index + 1])

    if (count <= min_h):
        c[l_index][r_index] = count
        return c[l_index][r_index]
    
    result = min_h
    
    a[l_index:r_index + 1] = list (map (lambda x: x - min_h, a[l_index:r_index + 1]))

    status = 0
    status2 = 0

    for i in range (count):
        if (a[l_index + i] > 0):
            status2 = 1
            if (status == 0):
                l_index2 = l_index + i
                status = 1
            if (status == 1):
                if (i == l_index2 and (l_index2 == r_index or a[l_index2 + 1] == 0)):
                    r_index2 = l_index + i
                    status = 0

                    result = result + find_min (l_index2, r_index2, a, c)
                elif (i != l_index2 and (i == count - 1 or a[l_index + i + 1] == 0)):
                    r_index2 = l_index + i
                    status = 0

                    result = result + find_min (l_index2, r_index2, a, c)
    
    if (status2 == 0):
        result = min (count, min_h)
        
    c[l_index][r_index] = min (count, result)
    return c[l_index][r_index]


n = int (input ())
a = str (input ()).split ()

a = list (map (int, a))

c = [[0 for i in range(n)] for j in range(n)]

c[0][n - 1] = find_min (0, n - 1, a, c)

print (c[0][n - 1])