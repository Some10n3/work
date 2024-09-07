def compact_name(name):
    if len(name) == 0:
        return name

    result = name[0]

    for i in range(1, len(name)):
        if name[i] != name[i - 1]:
            result += name[i]

    return result

name = input()

print(compact_name(name))
