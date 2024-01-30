'''def LinearSearch(array,n,k):
    for j in range(0,n):
        if(array[j]==k):
            return j
    return -1
array=[1,3,5,7,9]
k=1
n=len(array)
result= LinearSearch(array,n,k)
if(result==-1):
    print("element not found")
else:
    print("element found at index:",result)


def binarySearch(arr,k,low,high):
    while(low<=high):
        mid=low+(high-low)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,3,5,7,9]
k=5
result=binarySearch(arr,k,0,len(arr)-1)
if result!=-1:
    print("element found at index:",result)
else:
    print("element not found")'''



    
                
        
