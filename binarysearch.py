def binarysearch(arr,x,low,high):
    if high>=low:
        mid=low+(high-low)//2
        if(arr[mid]==x):
            return mid
        elif arr[mid]<x:
            return binarysearch(arr,x,mid+1,high)
        else:
            return binarysearch(arr,x,low,mid-1)
    return -1
arr=[1,2,3,4,5,6,7,8,9,10]
x=8
low=0
high=len(arr)-1
res=binarysearch(arr,x,low,high)
if res:

    print("element found at index:",res)
else:
    print("not found")
