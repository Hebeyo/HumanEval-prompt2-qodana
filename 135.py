def can_arrange(arr):
    ind=-1
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            ind=i
    return ind
