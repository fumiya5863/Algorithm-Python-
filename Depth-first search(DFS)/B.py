# 深さ優先探索テンプレート

N, M = map(int, map(int, input().split()))

# すべての頂点を未訪問にする
seen = [False]*N

# 深さ優先探索
def dfs(G, v):
    seen[v] = True # vの頂点を訪問済みにする

    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v) # 再帰関数の呼び出し

# グラフ作成
G = []
for n in range(N):
    G.append([])
# 無向グラフの場合
for m in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# 深さ優先探索
dfs(G, 0)
