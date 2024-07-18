# Divisors 包除原理
N = int(input())

waru3 = N // 3
waru5 = N // 5
waru15 = N // 15

print(waru3 + waru5 - waru15)