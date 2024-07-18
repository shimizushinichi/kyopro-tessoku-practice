#  Knapsack 1 二次元のDP（動的計画法）
N, W = map(int, input().split())
Weights = [0]
Values = [0]

for i in range(N):
    wi, vi = map(int, input().split())
    Weights.append(wi)
    Values.append(vi)

dp = [[0] * (W+1) for i in range(N+1)]
ans = 0
for n in range(1, N+1):
    for w in range(1, W+1):
        if Weights[n] <= w:
            dp[n][w] = max(dp[n-1][w], dp[n-1][w-Weights[n]] + Values[n])
        else:
            dp[n][w] = dp[n-1][w]
        ans = max(ans, dp[n][w])

print(ans)