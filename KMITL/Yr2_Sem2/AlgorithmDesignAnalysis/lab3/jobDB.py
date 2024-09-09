def max_jobs(jobs):
    # Sort jobs by finish time
    sorted_jobs = sorted(jobs, key=lambda x: x[1])
    
    count = 0
    last_finish = 0
    for start, finish in sorted_jobs:
        if start >= last_finish:
            count += 1
            last_finish = finish
    
    return count

if __name__ == "__main__":
    n = int(input())
    jobs = [tuple(map(int, input().split())) for _ in range(n)]
    print(max_jobs(jobs))

