def DRM (encrypted_message):
    mid = len(encrypted_message) // 2
    first_half = encrypted_message[:mid]
    second_half = encrypted_message[mid:]

    first_half_sum = 0
    second_half_sum = 0

    for i in range(len(first_half)):
        first_half_sum += ord(first_half[i]) - 65
        second_half_sum += ord(second_half[i]) - 65

    first_half = [chr((ord(first_half[i]) - 65 + first_half_sum) % 26 + 65) for i in range(len(first_half))]
    second_half = [chr((ord(second_half[i]) - 65 + second_half_sum) % 26 + 65) for i in range(len(second_half))]
    decrypted_message = ""

    for i in range(len(first_half)):
        decrypted_message += chr((ord(first_half[i]) - 65 + ord(second_half[i]) - 65) % 26 + 65)

    return decrypted_message
    
x = input()
print(DRM(x))