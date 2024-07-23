# Soccer 固定して全探索

N, K = map(int, input().split())
A = []
B = []

for i in range(N):
    Ai, Bi = map(int, input().split())
    A.append(Ai)
    B.append(Bi)

ans = 1
for a in range(1, 101):
    for b in range(1, 101):
        cnt = 0
        for i in range(N):
            if a <= A[i] and A[i] - a <= K and b <= B[i] and B[i] - b <= K:
                cnt += 1
        ans = max(ans, cnt)
print(ans)

# 勘違いしていたこと
# ①i番目の生徒を中心にA, Bの差がK以下ならカウントするという処理にした。
#   →最初はi番目自体をカウントに入れてなかったが、たまたまサンプルで3になった。
#   →i番目をカウントに入れるようにしたらサンプルが4になってしまった
# ②そもそも①のアプローチは誤りだった。
# これだとi番目とj番目はK以下だが、j+m番目とj+k番目の差がK以上なのにカウントするという不具合が起きる
# 本に書かれている通り、問題文の範囲内で取りうるA, Bの下限値の組み合わせを決めて、
# 下限値+Kまでの間に含まれる生徒数を数えるというアプローチにしないといけない。

# ans = 1

# for i in range(N):
#     cnt = 0
#     print(i)
#     for j in range(N):
#         if abs(A[i] - A[j]) <= K and abs(B[i] - B[j]) <= K:
#             print(A[i], A[j], abs(A[i] - A[j]))
#             print(B[i], B[j], abs(B[i] - B[j]))
#             cnt += 1
#     ans = max(ans, cnt)

# print(ans)

