# Game 4
N = int(input())
A = list(map(int, input().split()))

dp = [[0] * N for i in range(N)]

# 一番下のスコアを埋める
for i in range(N):
    dp[N-1][i] = A[i]

# dpを0始まりにしているので、偶数段は太郎が最大化して、奇数段は次郎が最小化を行う
for i in reversed(range(N-1)):
    for j in range(i+1):
        if i % 2 == 0:
            dp[i][j] = max(dp[i+1][j],dp[i+1][j+1])
        else:
            dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])

print(dp[0][0])