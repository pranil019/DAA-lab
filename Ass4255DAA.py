INF = float('inf')
n = 8
graph = [
    [0,   3, INF, 7, INF, INF, INF, INF],
    [3,   0,   2, INF, INF, INF, INF, INF],
    [INF, 2,   0,   1,   8, INF, INF, INF],
    [7, INF,   1,   0,   2,   3, INF, INF],
    [INF, INF, 8,   2,   0, INF,   4, INF],
    [INF, INF, INF, 3, INF,   0,   2,   6],
    [INF, INF, INF, INF, 4,   2,   0,   1],
    [INF, INF, INF, INF, INF, 6,   1,   0]
]

def floyd_warshall(graph):
    dist = [row[:] for row in graph] 

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def print_matrix(matrix):
    for row in matrix:
        for val in row:
            if val == INF:
                print("INF".ljust(5), end=" ")
            else:
                print(str(val).ljust(5), end=" ")
        print()

shortest_paths = floyd_warshall(graph)

print("Original Danger Levels:")
print_matrix(graph)

print("\nSafest Paths Between All Caves:")
print_matrix(shortest_paths) 