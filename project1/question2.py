def merge (l, r, mid, nums, result):
    n1 = mid - l + 1
    n2 = r - mid

    list1 = []
    list2 = []

    list1 = list1 + nums[l:mid + 1]
    
    list2 = list2 + nums[mid + 1:r + 1]
    
    i = 0
    j = 0

    while (i < n1 and j < n2):
        if (list1[i] > (2 * list2[j])):
            result[0] = result[0] + n1 - i
        
        if (list1[i] <= 2 * list2[j]):
            nums[l] = list1[i]
            i = i + 1
        else:
            nums[l] = list2[j]
            j = j + 1
        l = l + 1
    
    while (i < n1):
        nums[l] = list1[i]
        i = i + 1
        l = l + 1
    
    while (j < n2):
        nums[l] = list2[j]
        j = j + 1
        l = l + 1


def merge_sort (i, j, nums, result):
    if (i < j):
        mid = int ((i + j) / 2)

        merge_sort (i , mid, nums, result)
        merge_sort (mid + 1, j, nums, result)
        merge (i, j, mid, nums, result)


n = int (input ())
nums = str (input ()).split ()
nums = list (map (int, nums))

result = [0]

merge_sort (0, n - 1, nums, result)
print (result[0])