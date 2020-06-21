# AtCoder ABC84 D -2017-like NUmber
# 累積和とエラトステネスのふるいを使用
# 愚直に計算した場合には計算実行時間が間に合わない

Q = int(input())

# 十分な値の範囲を取っておく
MAX = 101010
A   = [1]*MAX

# 0と1は素数から除外
A[0] = 0
A[1] = 0

# エラトステネスのふるい
# 素数以外の値をふるい落とす
for n in range(2, MAX):
    i = n * 2
    while i < MAX:
        A[i] = 0
        i += n
# 2017に似た数を0から1にする
a = [0]*MAX
for n in range(MAX):
    if n % 2 == 0:
        continue
    if A[n] and A[(n+1)//2]:
        a[n] = 1

# 累積和
S = [0]*(MAX+1)
for n in range(MAX):
    S[n+1] = S[n] + a[n]

# l, rの範囲の総和を求める
B = []
for q in range(Q):
    l, r = map(int, input().split())
    r += 1
    B.append(S[r] - S[l])
for b in B:
    print(b)
