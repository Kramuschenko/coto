l=list(map(int,input().split()))
f=[]
m=0
for i in range(len(l)):
    m=0
    for j in range(i+1, len(l)):
        m1=l[i] ^ l[j]
        if m1 > m :
            m=m1
    f.append(m)
print(max(f))
