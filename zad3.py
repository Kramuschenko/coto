l = list(map(int, input().split()))
for i in range(len(l)):
    if l.count(l[i])==2:
        print(l[i])
        exit()
    