#AOJ0516 Maximum SUm

# 下記の処理では計算実行時間が間に合わない
# 1 <= K <= N <= 10**5
# 計算量 O(NK)
while True:
    N, K = map(int, input().split())
    if N == 0 and K == 0:
        break
    A = []
    for n in range(N):
        A.append(int(input()))
    res = 0
    for n in range(N - K + 1):
        total = 0
        for i in range(n, K + n):
            total += A[i]
        if res < total:
            res = total
print(res)

# 累積和を使用した解答
# 計算量 O(N) 
while True:
    N, K = map(int, input().split())
    if N == 0 and K == 0:
        break
    A   = []
    res = 0
    for n in range(N):
        A.append(int(input()))
    # 累積和
    S   = [0]*(N+1)
    for n in range(N):
        S[n+1] = S[n] + A[n]
    for n in range(N - K + 1):
        total = S[K + n]  - S[n]
        if res < total:
            res = total
print(res)