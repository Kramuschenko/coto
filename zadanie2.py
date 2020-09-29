l = list(map(int, input().split()))
target = int(input())
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == target:
            print(i, j)
            exit()
