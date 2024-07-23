# Tile Coloring 後ろから考える

# 最後の一手で必ず連続する3つは同じ色になる。
# -> 連続する3つは同じ色になる箇所が1つもない場合はNo
# 端っこから順に塗っていくという手法を取れば、最後の1手で3連続になる以外は自由に濡れる
N = int(input())
S = input()

ans = "No"
for i in range(N-2):
    if S[i] == S[i+1] and S[i+1] == S[i+2]:
        ans = "Yes"
        break

print(ans)