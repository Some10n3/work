def subsetSum(arr, n, sum):
    if sum == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] > sum:
        return subsetSum(arr, n-1, sum)
    return subsetSum(arr, n-1, sum) or subsetSum(arr, n-1, sum-arr[n-1])''

if __name__ == "__main__":
    arr = input().split()
    arr = [int(x) for x in arr]
    sum = int(input())
    n = len(arr)
    print(subsetSum(arr, n, sum))