# Prime Check 素数判定法
Q = int(input())

def is_prime(X):
    if X == 1:
        return False
    if X == 2:
        return True
    if X % 2 == 0:
        return False
    num = 3
    while num * num <= X:
        if X % num == 0:
            return False
        num += 2
    return True

for i in range(Q):
    X = int(input())
    if is_prime(X):
        print("Yes")
    else:
        print("No")