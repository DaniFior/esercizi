def bubble_sort(A : list) -> list :
    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                temp : int = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A

A : list = []
for i in range(1,1001):
    A.append(i)
bubble_sort(A)
print(A)