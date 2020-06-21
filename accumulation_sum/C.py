# エラストテネスのふるい O(nloglogn)
# 素数の値を表示
# 0, 1は含めない

# 標準入力
N = int(input())
# エラトステネスのふるい
A = [0]*100000 # 数字を格納する配列
for n in range(2, N+1):
    A[n] = n
for n in range(2, N+1):
    if A[n]:
        i = n * 2
        while i <= N:
            A[i] = 0
            i += n
for n in range(2, N+1):
    if A[n]:
        print(A[n])

# 1~10の数字の場合最初に2以外の2の倍数がふるいおとされて
# 次に3以外の3の倍数がふるい落とされ次には4といった風になっていく