# Combination 余りの計算（割り算、フェルマーの小定理）
n, r = map(int, input().split())
mod = 1000000007

def factorial_mod(n, mod):
    result = 1
    for i in range(2, n+1):
        result = result * i % mod
    return result

bunshi = factorial_mod(n, mod)
bunbo = factorial_mod(r, mod) * factorial_mod(n-r, mod) % mod

ans = bunshi * pow(bunbo, mod-2, mod) % mod # フェルマーの小定理を使う部分。全然理屈がわからん
print(ans)