#너비 우선 탐색

from collections import deque

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True

    while queue:
        v=queue.popleft()
        print(v,end=' ') #큐에서 하나의 원소를 뽑아 출력
        for i in graph[v]:
            if not visited[i]: #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
                queue.append(i)
                visited[i]=True




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

bfs(graph, 1, visited)