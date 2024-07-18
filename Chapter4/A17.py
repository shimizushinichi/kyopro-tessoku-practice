# Dungeon 2 一次元のDP(動的計画法)の復元

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0
dp[1] = A[0]

for i in range(2, N):
    dp[i] = min(dp[i-2] + B[i-2], dp[i-1] + A[i-1])

# 復元
ans = [N]
current_pos = N-1

while current_pos > 0:
    if dp[current_pos-1] + A[current_pos-1] == dp[current_pos]:
        ans.append(current_pos - 1 + 1) # 配列のインデックスに合わせるために+1
        current_pos = current_pos - 1
    else:
        ans.append(current_pos - 2 + 1) # 配列のインデックスに合わせるために+1
        current_pos = current_pos - 2

print(len(ans))
print(" ".join(map(str, ans[::-1])))