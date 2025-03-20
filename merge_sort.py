def merge_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        left_half=merge_sort(arr[:mid])
        right_half=merge_sort(arr[mid:])
    return merge(left_half, right_half)
def merge(left,right):
    sorted_arr = []
    i=j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])  
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
 
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

arr = [12, 11, 13, 5, 6, 7]
print("Given array is:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array is:" , sorted_arr)
