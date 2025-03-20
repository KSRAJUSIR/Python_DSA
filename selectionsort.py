def selectionsort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

data=[6,4,1,2,8,7,3,21]
         
print("list before sorting")
print(data)
selectionsort(data)
print("list after sorting")
print(data)