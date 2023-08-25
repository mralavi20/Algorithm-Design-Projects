import sys
sys.setrecursionlimit (2000)

def find_min (i, j, nums):
    if (i == j):
        return i
    
    l = find_min (i, int ((i + j) / 2), nums)
    r = find_min (int ((i + j) / 2) + 1, j, nums)

    if (nums[l] < nums[r]):
        return l
    else:
        return r

n = int (input ())
nums = input ().split ()

nums = list (map (int, nums))

min_index = find_min (0, n - 1, nums)

print ("(" + str (min_index) + "," + str (nums[min_index]) + ")")