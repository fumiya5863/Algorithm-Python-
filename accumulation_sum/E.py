# AtCoder ABC122 C -Get AC

# 計算実行時間が間に合わない
# 2 <= N <= 10**5, 1 <= Q <= 10**5
# 計算量O(NQ)
N, Q = map(int, input().split())
A = []
B = []
S = input()
for s in range(N):
    A.append(S[s])
for q in range(Q):
    l, r = map(int, input().split())
    s = A[l-1:r]
    cnt = 0
    for n in range(len(s)-1):
        if s[n] + s[n+1] == 'AC':
            cnt += 1
    B.append(cnt)
for b in B:
    print(b)

# 累積和を使用することで計算実行時間が間に合う
# 前処理O(N)
# 処理O(Q)
N, Q = map(int, input().split())
A = []
S = input()
s = [0]*(N+1)

# ACを探索
# 累積和
for n in range(N):
    if n+1 < N and S[n] == 'A' and S[n+1] == 'C':
        s[n+1] = s[n] + 1
    else:
        s[n+1] = s[n]

# クエリの処理
for q in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    A.append(s[r]-s[l])
for a in A:
    print(a)