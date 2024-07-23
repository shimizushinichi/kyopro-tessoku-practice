# Interval Scheduling Problem 区間スケジューリング問題 貪欲法

N = int(input())
LR = []
for i in range(N):
    Li, Ri = map(int, input().split())
    LR.append([Li, Ri])

# 終了時刻が速い順に見ていく
# 終了時刻で昇順にソートしてそれぞれ開始時刻に間に合うかどうかをチェックする処理を実装する
LR = sorted(LR, key=lambda x: x[1])

current_time = 0
ans = 0

for i in range(N):
    if current_time <= LR[i][0]:
        ans += 1
        current_time = LR[i][1]

print(ans)