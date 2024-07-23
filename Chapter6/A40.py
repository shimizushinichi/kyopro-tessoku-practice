# Triangle 個数を考える
import math

N = int(input())
A = list(map(int, input().split()))
A_nums = [0] * 101

for a in A:
    A_nums[a] += 1

ans = 0
for A_num in A_nums[1:]:
    if A_num >= 3:
        ans += math.comb(A_num, 3)

print(ans)