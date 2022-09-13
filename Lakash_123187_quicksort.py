def quicksort(A,p,r): #p is left index, r is right index
    if p < r: # if left is small then right
        q=partition(A,p,r) #q is positon for partition
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def partition (A,p,r):
    x=A[r] 
   # j=r
    #i= p-1
    i=p
    j=r-1
    while i<j:
        while i < r and A[i]<x:
            i=i+1
        while j>p and A[j]>=x:
            j=j-1
        if i<j:
            A[i],A[j]=A[j],A[i]
    if A[i] > x:
        A[i],A[r]=A[r],A[i]
    return i
    #for i in range (i,j):
     #   if A[j] <= x:
      ##     A[i],A[j]=A[j],A[i]
        
    #A[i+1],A[r]=A[r],A[i+1]
    #return i+1 
A=[15,13,9,5,12,8,7,11]
quicksort(A,0,len(A)-1)
print(A)



