#동빈이는 NXM 크기의 미로에 갇혀있다. 미로에는 여러마리의 괴물이 있어 이를 피해 탈출해야 한다. 동빈이의 위치는 (1,1)이고 출구는(n,M에 존재한다.)
#한번에 한칸씩 이동 가능하며, 괴물이 있는 위치는 0, 없는 위치는 1이다. 탈출하기 위해 움직여야 하는 칸의 개수를 구하시오.
#시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하는 BFS를 사용하는 것이 좋다.
from collections import deque
n,m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0] #상, 하, 좌, 우의 네 방향을 정의
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))  #append에 단일값을 넣을때만 append(x)의 형식으로, 다중 값을 넣을 때는 append((x,y))를 쓴다.
     #큐가 빌 때까지 반복
    while queue:
        x,y=queue.popleft()
        #현재 방향에서 네 방향으로의 위치 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #벽인 경우 무시
            if graph[nx][ny]==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1 #graph[nx][ny]는 이동한 노드, graph[x,y]는 이동하기 전 기존 노드
                queue.append((nx,ny))
    return graph[n-1][m-1] #가장 오른쪽 아래까지의 최단 거리 반환
    
print(bfs(0,0))
                

