import heapq

def dijkstra(node_info):
    """各ノードの最短経路を求める"""
    nodes_min = {k:float('inf') for k in range(V)}   # node の初期化. 最短経路が更新されていく．
    
    node_paths = []    
    heapq.heappush(node_paths, [0, [0]])        # 最初は 0 node． [dist, [path]] の第1引数を基準に常にソートされている．
    
    while len(node_paths) > 0:
        _, node_path = heapq.heappop(node_paths)
        dist_from = node_path[0]
        last_node = node_path[-1]               # path の一番後ろのノードを次に探索する．
        for path in node_info[last_node]:
            node, dist_to =  path[0], path[1]
            # 更新条件
            if dist_from + dist_to < nodes_min[node]:
                nodes_min[node] = dist_from + dist_to
                #print(node_path, node)
                heapq.heappush(node_paths, [nodes_min[node], node_path + [node]]) # heap により，そのノードにおいて最短のものが常に先に取り出される．
            
        # 全ノードの最短距離が求まった．
        #print(node_paths, nodes_min)
        if node_paths == []:
            return nodes_min


if __name__ == '__main__':
    V, E, r = map(int, input().split())
    STD = [list(map(int, input().split())) for _ in range(E)]
    
    # データ成型
    node_info = [[] for _ in range(V)]
    for start, end, dist in STD:                # 各エッジの start, end, dist
        node_info[start].append((end, dist))    # node[0] は A からのパス(node)と距離
    
    min_path_for_each_node = dijkstra(node_info)
    for min_dist in min_path_for_each_node.values():
        print(min_dist)


"""
4 5 0
0 1 1
0 2 4
1 2 2
2 3 1
1 3 5
"""