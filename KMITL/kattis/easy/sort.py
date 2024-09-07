def sort_student_names(names):
    # Sort the names based on the first two letters using a stable sort
    names.sort(key=lambda x: x[:2])

    return names

names = []
# Read input
while True:
    n = int(input())
    if n == 0:
        break
    
    case = []
    for i in range(int(n)):
        N = input()
        case.append(N)
    
    sort_student_names(case)
    names.append(case)

for case in names:
    for name in case:
        print(name)
    print()