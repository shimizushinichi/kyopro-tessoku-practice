# Game 2 二ム
# 物真似戦略をするのが必勝法らしい
# 山が2個の場合、A1=A2 => 後手必勝、A1!=A2 => 先手必勝
# 山がN個の場合、
# A1 XOR A2 XOR ... XOR AN = 0 => 後手必勝
# A1 XOR A2 XOR ... XOR AN != 0 => 先手必勝
# 理屈は何もわからない

N = int(input())
A = list(map(int, input().split()))

XOR_sum = A[0]
for i in range(1, N):
    XOR_sum = XOR_sum ^ A[i]

if XOR_sum == 0:
    print("Second")
else:
    print("First")