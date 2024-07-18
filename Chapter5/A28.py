# Blackboard 余りの計算
N = int(input())
ans = 0
mod = 10000
for i in range(N):
    Ti, Ai = input().split()
    Ai = int(Ai)
    if Ti == "+":
        ans = ans + Ai
    elif Ti == "-":
        ans = ans - Ai
        if ans < 0:
            ans += 10000

    elif Ti == "*":
        ans = ans * Ai
    ans = ans % mod
    print(ans)