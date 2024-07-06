# Winter in ALGO Kingdom
H, W, N = map(int, input().split())
Z = [[0] * (W + 2) for i in range(H + 2)]

for n in range(N):
    A, B, C, D = map(int, input().split())
    Z[A][B] += 1
    Z[A][D+1] -= 1
    Z[C+1][B] -= 1
    Z[C+1][D+1] += 1

# 横方向に累積和をとる
for h in range(1, H+1):
    for w in range(1, W+1):
        Z[h][w] += Z[h][w-1]

# 縦方向に累積和をとる
for w in range(1, W+1):
    for h in range(1, H+1):
        Z[h][w] += Z[h-1][w]

for h in range(1, H+1):
    print(" ".join(map(str, Z[h][1:W+1])))