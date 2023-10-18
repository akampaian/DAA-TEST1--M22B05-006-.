def insertionsort(A, n):
    for pos in range(1, n):
        nextpos = pos
        while nextpos > 0 and A[nextpos] < A[nextpos - 1]:
            swap(A, nextpos, nextpos - 1)
            nextpos = nextpos - 1
    return A

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]