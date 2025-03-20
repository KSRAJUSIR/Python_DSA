def insertion_sort(array):
    n=len(array)
    for i in range(1,n):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1
            array[j+1]=key
arr=[20,10,35,48,7,3]
insertion_sort(arr)
print("sorted array:",arr) 