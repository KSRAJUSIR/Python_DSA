def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        less_than_pivot=[x for x in arr[1:] if x<=pivot]
        greater_than_pivot=[x for x in arr[1:] if x>=pivot]
    return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)
arr=[7,10,8,9,5]
sorted_arr=quick_sort(arr)
print("sorted array is:",sorted_arr) 