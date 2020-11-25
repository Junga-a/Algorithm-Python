#깊이 우선 탐색법
def dfs(graph, v, visited):  #v는 몇 번 노드인지, visited는 방문 정보 리스트
    visited[v]=True #현재 노드를 방문 처리
    print(v,end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph=[
    [],  #노드의 번호가 0이 아니라 1부터 시작할 때에는 0의 index는 그냥 비워두는게 좋다.
    [2,3,8],  #1번 노드는 2,3,8과 연결
    [1,7], #2번 노드는 1,7과 연결
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9 # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)

dfs(graph, 1, visited)