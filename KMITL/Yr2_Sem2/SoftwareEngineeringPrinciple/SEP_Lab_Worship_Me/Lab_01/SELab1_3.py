def binary_search(num, sequence):
    mid = len(sequence) // 2
    
    if sequence[mid] == num and len(sequence) >= 1:
        return mid
    
    elif len(sequence) == 1:
        return False

    elif sequence[mid] < num:
        b = binary_search(num, sequence[mid:])
        if b != False:
            return mid + b
        return b
    
    elif sequence[mid] > num:
        b = binary_search(num, sequence[:mid])
        if b != False:
            return mid + b
        return b


if __name__ == "__main__":
    print(binary_search(7, [2, 3, 4, 7, 8]))
    print(binary_search(6, [2, 3, 4, 6, 8]))