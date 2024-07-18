# Subset Sum 二次元のDP（動的計画法）
N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (S+1) for i in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    for j in range(0, S+1): #ここを1始まりにしてWAだった
        if dp[i-1][j] == True: #i枚目を使わなくても達成できているケース
            dp[i][j] = True
        elif j >= A[i-1] and dp[i-1][j-A[i-1]] == True: #i枚目を選択すると達成できるケース
            dp[i][j] = True

if dp[N][S]:
    print("Yes")
else:
    print("No")