# LCS 最長共通部分列
# こっちも参考になる内容だった: https://qiita.com/sh4ft3/items/bc86b15ee9d69d61a6c2
# LCS問題では、与えられた2つの文字列の間で共通する部分列の中で最も長いものを見つけることが目標です。部分列とは、元の文字列から一部の文字を削除して残った文字列のことを指しますが、文字の順序は保持されなければなりません。(ChatGPT)
S = input()
T = input()

dp = [[0] * (len(T)+1) for i in range(len(S)+1)]

for i in range(1, len(S)+1):
    for j in range(1, len(T)+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(S)][len(T)])