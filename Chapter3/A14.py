# Four Boxes 半分全列挙
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# 集合を使って探索する場合は202ms 298132KB
P = []
Q = set()

for i in range(N):
    for j in range(N):
        P.append(A[i] + B[j])

for i in range(N):
    for j in range(N):
        Q.add(C[i] + D[j])

ans = "No"
for i in range(len(P)):
    if K - P[i] in Q:
        ans = "Yes"
        break
print(ans)

# ソートした配列にして二分探索を使う場合は256ms 225324KB
# import bisect
# P = []
# Q = []

# for i in range(N):
#     for j in range(N):
#         P.append(A[i] + B[j])

# for i in range(N):
#     for j in range(N):
#         Q.append(C[i] + D[j])

# Q.sort()

# ans = "No"
# for i in range(len(P)):
#     bisect_result = bisect.bisect_left(Q, K - P[i])
#     if bisect_result < len(P) and K - P[i] == Q[bisect_result]:
#         ans = "Yes"
#         break
# print(ans)