def linear_search(array,target):
    for i,ele in enumerate(array):
        if ele==target:
            print("element found:",ele,i)
            break
array=list(map(int,input().split()))
target=int(input())
linear_search(array,target)

        