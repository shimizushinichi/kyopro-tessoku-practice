# Change and Reverse データの持ち方を工夫する
N, Q = map(int, input().split())
A = [i for i in range(N+1)]
is_reversed = False

for i in range(Q):
    query = list(map(int, input().split()))
    if len(query) == 3:
        X = query[1]
        if is_reversed:
            X = N+1-X
        A[X] = query[2]
    elif len(query) == 1:
        is_reversed = not is_reversed
    elif len(query) == 2:
        X = query[1]
        if is_reversed:
            X = N+1-X
        print(A[X])
