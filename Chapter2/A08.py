# Two Dimensional Sum
"""
X = [
    [x, x, x, x, x],
    [x, x, x, x, x],
    [x, x, x, x, x],
    [x, x, x, x, x],
    [x, x, x, x, x],
]
SX = [
    [0, 0, 0, 0, 0, 0],
    [0, x, x, x, x, x],
    [0, x, x, x, x, x],
    [0, x, x, x, x, x],
    [0, x, x, x, x, x],
    [0, x, x, x, x, x],
]
"""

H, W = map(int, input().split())
X = []
for i in range(H):
    X.append(list(map(int, input().split())))
SX = [[0] * (W+1) for i in range(H+1)]

# 横方向に累積和をとる
for h in range(1, H+1):
    for w in range(1, W+1):
        SX[h][w] = SX[h][w-1] + X[h-1][w-1]

# 縦方向に累積和をとる
for w in range(1, W+1):
    for h in range(1, H+1):
        SX[h][w] = SX[h][w] + SX[h-1][w]

Q = int(input())
for q in range(Q):
    A, B, C, D = map(int, input().split())
    print(SX[C][D] - SX[A-1][D] - SX[C][B-1] + SX[A-1][B-1])
    