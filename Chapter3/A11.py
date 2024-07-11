# Binary Search 1
# import bisect

N, X = map(int, input().split())
A = list(map(int, input().split()))

# print(bisect.bisect_right(A, X))

def binary_search(A, X):
    L = 0
    R = len(A) - 1
    while (L <= R):
        M = (L + R) // 2
        if X < A[M]:
            R = M - 1
        elif X > A[M]:
            L = M + 1
        else:
            return M

print(binary_search(A, X) + 1)