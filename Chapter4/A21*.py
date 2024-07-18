# Block Game 区間DP
# 詰まったのでskip

N = int(input())
P = []
A = []
for i in range(N):
    Pi, Ai = map(int, input().split())
    P.append(Pi)
    A.append(Ai)

dp = [[0] * (N+1) for i in range(N+1)]
dp[0] = [None] * (N+1)
for i in range(1, N+1):
    dp[i][0] = None

