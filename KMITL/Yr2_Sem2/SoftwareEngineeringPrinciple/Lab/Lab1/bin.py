def binary_Search(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_Search(arr, l, mid - 1, x)
        else:
            return binary_Search(arr, mid + 1, r, x)
    else:
        return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 11
    result = binary_Search(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element is present at index %d" %result)
    else:
        print("Element %d is not present in array" %x)
    x = 10
    result = binary_Search(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element is {0} present at index {1}".format(x, result))
    else:
        print("Element %d is not present in array" %x)