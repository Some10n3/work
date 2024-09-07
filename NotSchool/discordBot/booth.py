def boothRental(arr):
    lenn = len(arr)

    if lenn == 0:
        return []

    if lenn == 1:
        return [arr]

    # Initialize dp with lists containing single elements
    dp = [[x] for x in arr]

    for i in range(0, lenn):
        for j in range(i, lenn):
            if arr[i] > arr[j] and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [arr[i]]

    # Find the list with the maximum length
    max_length = max(len(subseq) for subseq in dp)
    result = [subseq for subseq in dp if len(subseq) == max_length]
    print(dp)

    return result

if __name__ == "__main__":
    user_input = input().split()
    arr = [int(x) for x in user_input]
    result = boothRental(arr)
    print("Longest Increasing Subsequences:", result)
