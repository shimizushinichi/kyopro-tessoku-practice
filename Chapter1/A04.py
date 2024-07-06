# Binary Representation 1
# N = int(input())
# ans = format(N, '010b')
# print(ans)

N = int(input())
tmp_N = N
ans = ""
for i in range(10):
    mod = tmp_N % 2
    tmp_N = tmp_N // 2
    ans = str(mod) + ans
print(ans)