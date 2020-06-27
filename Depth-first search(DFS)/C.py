# 行きがけ順と帰りがけ順

N, M = map(int, input().split())
seen = [False]*N
first_order = [0]*N # 行きがけ順
last_order = [0]*N  # 帰りかけ順
first_ptr = 0
last_ptr = 0

# 深さ優先探索
def dfs(G, v):
    global first_ptr
    global last_ptr
    first_order[v] = first_ptr
    first_ptr = first_ptr + 1

    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v)
    
    last_order[v] = last_ptr
    last_ptr = last_ptr + 1

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
