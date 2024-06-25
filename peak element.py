
a=[1,2,3,4,5]
def search(a):
    if a[0]!=1:
        return 1
    for i in range(len(a)-1):
        if a[i]+1!=a[i+1]:
            return(a[i]+1)
b=search(a)
print(b)