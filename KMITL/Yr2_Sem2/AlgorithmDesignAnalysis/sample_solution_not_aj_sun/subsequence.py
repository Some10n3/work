def findlongestsubsequence(arr):
    n = len(arr)
    lis = [1]*n
    for i in range (1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
    return max(lis)

def main():
    s = []
    in1 = input()
    for i in in1.split():
        s.append(int(i))
    print(findlongestsubsequence(s))
    
main()
