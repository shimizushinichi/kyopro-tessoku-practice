# Compression 座標圧縮
import bisect
N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(set(A))

ans = []
for a in A:
    ans.append(bisect.bisect_right(sorted_A, a))

print(" ".join(map(str, ans)))