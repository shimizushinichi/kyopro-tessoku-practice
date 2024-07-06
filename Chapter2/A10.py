# Resort Hotel
N = int(input())
A = list(map(int, input().split()))
D = int(input())
from_left = [0] * N
from_left[0] = A[0]
from_right = [0] * N
from_right[-1] = A[-1]

for i in range(1, N):
    from_left[i] = max(from_left[i-1], A[i])

for i in reversed(range(0, N-1)):
    from_right[i] = max(from_right[i+1], A[i])

for d in range(D):
    L, R = map(int, input().split())
    print(max(from_left[L-2], from_right[R]))