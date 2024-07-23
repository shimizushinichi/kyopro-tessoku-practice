# Travel 2 足された回数を考える 主客転倒テクニック
N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

# A1だけを考えると M * A1 + M * B + (C1+...+CN)
# A2だけを考えると M * A2 + M * B + (C1+...+CN)
# ANだけを考えると M * AN + M * B + (C1+...+CN)
# A1~ANを全部足すとM * (A1+...+AN) + N * M * B + N * (C1+...+CN)

print(M * sum(A) + N * M * B + N * sum(C))