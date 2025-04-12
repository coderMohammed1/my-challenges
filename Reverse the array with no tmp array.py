# do it yourself 🫡
arr=[1,2,3,4,5,6,7]
k=-1
for i in range(int(len(arr)/2)):
    tmp=arr[i]
    arr[i]=arr[k]
    arr[k]=tmp
    k=k-1
    
for j in arr:
    print(j)
