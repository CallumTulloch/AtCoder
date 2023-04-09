import heapq
import copy
import sys

def dijkstra(adj_mtx, num_node, Start, Goal):
    node = [float('inf')] * num_node    #スタート地点以外の値は∞で初期化
    node[Start] = 0     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, [Start]])
    while len(node_name) > 0:
        _, min_point = heapq.heappop(node_name)
        last = min_point[-1] 
        if last == Goal:
            return min_point, node  #道順とコストを出力させている

        for goal in range(num_node):
            cost = adj_mtx[last][goal]
            if cost != -1:
                #更新条件
                if node[last] + cost < node[goal]:
                    node[goal] = node[last] + cost     #更新
                    #ヒープに登録．ソートは各要素の最初の次元（コスト）を基準．
                    heapq.heappush(node_name, [node[last] + cost, min_point + [goal]])
    return -1,-1

if __name__ == '__main__':

    N, K = map(int, input().split())
    x = [list(map(int, input().split()))*K for _ in range(N)]
    X=[copy.deepcopy(ele) for _ in range(K) for ele in x]
    Q = int(input())
    ST = [list(map(int, input().split())) for _ in range(Q)]
    
    adj_mtx = [[-1 for _ in range(N*K)] for _ in range(N*K)]
    for r_ids,row in enumerate(X):
        for c_idx, col in enumerate(row):
            if col == 1:
                adj_mtx[r_ids][c_idx] = 1

    for s,t in ST:
        node_num = N*K
        Start = s - 1
        Goal = t - 1
        opt_root, opt_cost = dijkstra(adj_mtx, node_num, Start, Goal)

        if opt_root == -1:
            print(-1)
        else:
            print(opt_cost[Goal] if opt_cost[Goal] != float('inf') else -1)
