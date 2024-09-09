def max_earning(n, jobs):
    # Sort jobs based on finish times
    jobs.sort(key=lambda x: x[1])

    # Initialize an array to store maximum total earnings for each job
    dp = [0] * n

    # Base case: the maximum total earning for the first job is its own earning
    dp[0] = jobs[0][2]

    # Iterate through the jobs
    for i in range(1, n):
        # Find the latest non-conflicting job
        latest_non_conflicting = -1
        for j in range(i - 1, -1, -1):
            if jobs[j][1] <= jobs[i][0]:
                latest_non_conflicting = j
                break

        # Update the maximum total earning for the current job
        dp[i] = max(dp[i - 1], jobs[i][2] + (dp[latest_non_conflicting] if latest_non_conflicting != -1 else 0))

    # The final result is the maximum total earning for the last job
    return dp[-1]

# Read the number of jobs
n = int(input())

# Read the jobs as lines of strings, then split each line
jobs = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_earning(n, jobs))




