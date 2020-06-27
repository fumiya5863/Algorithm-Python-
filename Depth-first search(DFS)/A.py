# 深さ優先探索の入力受け取り

# 頂点数と変数を受け取る
N, M = map(int, input().split())

# グラフ作成
G = []
for n in range(N):
    G.append([])
for m in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    # 無向グラフの場合
    # G[b].append(a)