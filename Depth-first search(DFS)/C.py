# 行きがけ順と帰りがけ順

# 入力受け取り
N, M = map(int, input().split())

seen        = [False]*N
first_order = [0]*N # 行きがけ順
last_order  = [0]*N  # 帰りかけ順
first   = 0
last    = 0

# 深さ優先探索
def dfs(G, v):
    global first
    global last

    # 行きかけ順に1プラス
    first_order[v] = first
    first = first + 1

    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v)
    
    # 帰りがけ順に1プラス
    last_order[v] = last
    last = last + 1

    
# # タイムスタンプの場合
# ptr = 0
# def dfs(G, v):
#     global ptr

#     first_order[v] = ptr
#     ptr = ptr + 1

#     seen[v] = True
#     for next_v in G[v]:
#         if seen[next_v]:
#             continue
#         dfs(G, v)
#     last_order[v] = ptr
#     ptr = ptr + 1

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

for n in range(N):
    print('{} {} {}'.format(n, first_order[n], last_order[n]))
