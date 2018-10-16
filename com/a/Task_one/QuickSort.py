def exchange(arr, l, h):
    t = arr[l]
    arr[l] = arr[h]
    arr[h] = t


def QuickSort(arr, low, high):
    l = low
    h = high
    p = arr[low]
    while l < h:
        while l < h and arr[h] > p: h -= 1
        if l < h:
            exchange(arr, l, h)
        while l < h and arr[l] < p: l += 1
        if l < h:
            exchange(arr, l, h)
        if l > low: QuickSort(arr, low, l - 1)
        if h < high: QuickSort(arr, l + 1, high)


print("Please input the list: ", end=" ")
arr = [int(i) for i in input().split(" ")]
QuickSort(arr, 0, len(arr) - 1)
print("The result is ", end="")
print(arr)
