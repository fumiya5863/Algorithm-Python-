# AtCoder AGC023 A -Zero-Sum Ranges 

# 累積和を使用
N = int(input())
A = list(map(int, input().split()))

# 累積和
S = [0]*(N+1)
for n in range(N):
    S[n+1] = S[n] + A[n]

# 総和が0になる物を見つけるので
# 例) 2 - 2 = 0, 4 - 4 = 0
# 辞書にどの数値が何個あるか分かるように格納する
B = {}
for s in range(len(S)):
    B[S[s]] = 0
for s in range(len(S)):
    B[S[s]] += 1

# 集計処理
res = 0
for v in B.values():
    # 組み合わせ
    # 例) 4C2 = 4*3 / 2
    res += v * (v - 1) // 2
print(res)