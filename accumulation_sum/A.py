# 配列のサイズを取得
N = int(input())
A = list(map(int, input().split()))

# 累積和
S = [0]*(N+1)  # S[0] = 0になる
for n in range(N):
    S[n+1] = S[n] + A[n]

# 累積和の実装
# 2 3 4 5 6
# S0 = 0
# S1 = 2
# S2 = S1(2) + 3
# S3 = S2(2 + 3) + 4
# S4 = S3(2 + 3 + 4) + 5
# S5 = S4(2 + 3 + 4 + 5) + 6

# 区間の総和を求める時
left  = int(input())
right = int(input())
print(S[right] - S[left])
