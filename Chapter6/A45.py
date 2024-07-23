# Card Elimination 不変量に着目する

N, C = input().split()
A = input()

score = 0

for a in A:
    if a == "B":
        score += 1
    elif a == "R":
        score += 2

last = ""
if score % 3 == 0:
    last = "W"
elif score % 3 == 1:
    last = "B"
else:
    last = "R"

if last == C:
    print("Yes")
else:
    print("No")