# Close Pairs
N, K = map(int, input().split())
A = list(map(int, input().split()))

# しゃくとり法
ans = 0
Ri = 0
for i in range(N-1):
    while (Ri+1 < N and A[Ri+1] - A[i] <= K):
        Ri += 1
    ans += (Ri + 1) - (i + 1)

print(ans)

# # 単純にO(n^2)でやってみたらTLE
# ans = 0
# tmp = 0
# for i in range(N-1):
#     for j in range(i+1, N):
#         if A[j] - A[i] <= K:
#             ans += 1
#         else:
#             break
# print(ans)

# # 二分探索でやってみたらTLE
# def binary_search_max_point(A, K, base):
#     if A[0] - base > K:
#         return 0
#     L = 0
#     R = len(A) - 1
#     while L < R:
#         M = (L + R) // 2
#         if A[M] - base < K:
#             L = M + 1
#         elif A[M] - base > K:
#             R = M - 1
#         else:
#             return L + 1
#     return L + 1

# ans = 0

# for i in range(N-1):
#     ans += binary_search_max_point(A[i+1:], K, A[i])

# print(ans)

