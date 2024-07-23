# Travel 3 問題を言い換える

# 人iを区別する問題ではないので、向きを変えることは考えなくてよい
# E方向に進む場合は(L - Ai)秒, W方向に進む場合はAi秒でトンネルの外に出ると考えられる

N, L = map(int, input().split())
ans = -1
for i in range(N):
    Ai, Bi = input().split()
    Ai = int(Ai)
    if Bi == "E":
        ans = max(ans, L - Ai)
    else:
        ans = max(ans, Ai)

print(ans)
