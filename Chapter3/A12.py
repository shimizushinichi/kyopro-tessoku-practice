N, K = map(int, input().split())
A = list(map(int, input().split()))

def canPrintK(A, sec, K):
    S = 0
    for a in A:
        S += sec // a
    if S >= K:
        return True
    else:
        return False

L = 0
R = 10**9

while L < R:
    M = (L + R) // 2
    if canPrintK(A, M, K):
        R = M
    else:
        L = M + 1

print(L)