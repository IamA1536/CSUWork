def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    num = int(len(arr) / 2)
    left = MergeSort(arr[:num])
    right = MergeSort(arr[num:])
    return Merge(right, left)


def Merge(left, right):
    r = 0
    l = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result


print("Please input the list: ", end=" ")
arr = [int(i) for i in input().split(" ")]
print("result is ", end="")
print(MergeSort(arr))
