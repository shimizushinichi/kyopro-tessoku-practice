# Game 1 石取ゲーム

N, A, B = map(int, input().split())

dp = [None] * (N+1)

for i in range(N+1):
    # もう取れない状態は「負けの状態」
    if i < min(A, B):
        dp[i] = False
    # A個かB個を取って相手を負けの状態にできるのは「勝ちの状態」
    elif dp[i-A] == False or dp[i-B] == False:
        dp[i] = True
    # A個とってもB個とっても相手が勝ちの状態になるのは「負けの状態」
    elif dp[i-A] == True and dp[i-B] == True:
        dp[i] = False

if dp[N]:
    print("First")
else:
    print("Second")