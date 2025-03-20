def max_heap(A,K):
    l=left(K)
    r=right(K)
    if l<len(A) and A[l]>A[K]:
        largest=l
    else:
        largest=K
    if r<len(A) and A[r]>A[largest]:
        largest=r
    if largest!=K:
        A[K],A[largest]=A[largest],A[K]

def left(K):
    return 2*K+1
def right(K):
    return 2*K+2

def build_tree(A,K):
    n=len(A)//2
    for i in range(n-1,-1,-1):
        max_heap(A,i)
A=[3,9,2,1,4,5]
build_tree(A)
print("max_heap",A)
