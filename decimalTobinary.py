T=int(input())
k=[]
while T>0:
    k.append(T%2)
    T=T//2
print("".join([str(k[x]) for x in range(len(k)-1,-1,-1)]))

