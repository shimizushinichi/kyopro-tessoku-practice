# Event Attendance
D = int(input())
N = int(input())
S = [0] * (D + 2)
for i in range(N):
    L, R = map(int, input().split())
    S[L] += 1
    S[R+1] -= 1

ans = [0]
for i in range(1, len(S)-1):
    ans.append(ans[i-1] + S[i])
    print(ans[i])
