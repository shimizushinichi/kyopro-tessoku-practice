# Black Company 1 上限値を考える
D, N = map(int, input().split())
limit = [24] * (D+1) # インデックスと日数を合わせるため、配列の個数はD+1個とする
limit[0] = 0 # 0日目は0とする

# 全ての日について、最も短い制限の労働時間をlimitに入れる
for i in range(N):
    Li, Ri, Hi = map(int, input().split())
    for j in range(Li, Ri+1):
        limit[j] = min(limit[j], Hi)

print(sum(limit))