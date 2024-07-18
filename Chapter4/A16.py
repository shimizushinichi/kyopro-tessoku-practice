# Dungeon 1 一次元のDP(動的計画法)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0
dp[1] = A[0]

for i in range(2, N):
    dp[i] = min(dp[i-2] + B[i-2], dp[i-1] + A[i-1])

print(dp[-1])