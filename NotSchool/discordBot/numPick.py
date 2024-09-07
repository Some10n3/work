def numPick(arr, prev_num):
    if len(arr) == 0:
        return True

    first_num_valid = abs(arr[0] - prev_num) <= 9
    last_num_valid = abs(arr[-1] - prev_num) <= 9

    if first_num_valid and numPick(arr[1:], arr[0]):
        return True
    elif last_num_valid and numPick(arr[:-1], arr[-1]):
        return True
    else:
        return False

if __name__ == "__main__":
    user_input = input().split()
    arr = [int(x) for x in user_input]

    if numPick(arr[1:], arr[0]) or numPick(arr[:-1], arr[-1]):
        print("Yes")
    else:
        print("No")
