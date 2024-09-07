def avg_Character(str):
    for s in str:
        return chr(int(sum(ord(s) for s in str) / len(str)))

print(avg_Character(input()))