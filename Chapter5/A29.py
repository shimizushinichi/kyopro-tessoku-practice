# Power 余りの計算（繰り返し二乗法）
a, b = map(int, input().split())
mod = 10**9 + 7

# a = 5, b = 23のときを考える。
# bは二進数にすると10111なので23 = 1 + 2 + 4 + 16で表せられる
# なので ans = 5**1 * 5**2 * 5**4 * 5**16で求められる
# 2**29 < 10**9 < 2**30なので2**0乗~2**30乗まで計算すればよいので、
# i = 0 ~ 30について、23 >> i == 1なら5**(2**i)をansに掛けてmodで割るという流れで良い
# ansに掛ける数はi-1のときに掛けるか検討した数を2乗したものを使う
p = a
ans = 1
for i in range(0, 30):
    if b >> i & 1 == 1:
        ans = ans * p % mod
    p = p * p % mod

print(ans)

# python3ではpowが繰り返し2乗法で実装されている
# pow(base, exp, mod=None)
# ans = pow(a, b, mod)
# print(ans)