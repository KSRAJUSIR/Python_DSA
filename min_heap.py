def left(K):
    return K*2+1

def right(K):
    return K*2+2

def min_heap(A,K):
    l=left(K)
    r=right(K)
    if l<len(A) and A[l]<A[K]:
       smallest=l
    else:
        smallest=K
    if r<len(A) and A[r]<A[smallest]:
        smallest=r
    else:
        smallest!=K
        A[K],A[smallest]=A[smallest],A[K]
def build_tree(A):
    n=len(A)//2
    for k in range(n-1,-1,-1):
        min_heap(A,k)
A=[3,9,2,1,4,5]
build_tree(A)
print('build_tree',A)
