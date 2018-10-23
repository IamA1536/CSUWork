def dijkstra(g, src):
    if g is None:
        return None
    nodes = [i for i in range(len(g))]
    visited = []
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    dis = {src: 0}
    for i in nodes:
        dis[i] = g[src][i]
    #    path = {src: {src: []}}
    n = pre = src
    while nodes:
        mid = float('inf')
        for v in visited:
            for d in nodes:
                if g[src][v] + g[v][d] < mid:
                    mid = g[src][v] + g[v][d]
                    n = d
                #   pre = v
        dis[n] = mid
        #    path[src][n] = [i for i in path[src][pre]]
        #    path[src][n].append(n)
        visited.append(n)
        nodes.remove(n)

    return dis
    # , path


if __name__ == "__main__":
    g = graph_list = [[0, 2, 1, 4, 5, 1],
                      [1, 0, 4, 2, 3, 4],
                      [2, 1, 0, 1, 2, 4],
                      [3, 5, 2, 0, 3, 3],
                      [2, 4, 3, 4, 0, 1],
                      [3, 4, 7, 3, 1, 0]]
    #    n = int(input("Please input the number of point: "))
    #    for i in range(n):
    #        g.append([])
    #        for j in range(n):
    #            g[i].append(int(input("Please input the path from {0} to {1}: ".format(i, j))))
    #    m = int(input("Please input the src: "))
    dis = dijkstra(g, 0)
    print(dis)
