#어떤 나라에는 N개의 도시가 있고, 각 도시는 보내고자 하는 메시지가 있을 경우 다른 도시를 거치지 않고 해당 도시로 직접적으로 메시지를 보내야 하고, 
# 메시지를 보낼때는 일정 시간이 소요된다. 어느날 C도시에서 위급 상황이 발생하여 최대한 많은 도시로 메시지를 보내고자 하는데, 
# 메시지는 도시 c에서 출발하여 각 도시 사이에 설치된 통로(M개)를 거쳐 최대한 많이 퍼쳐나간다. 
# 도시 C에서 보낸 메시지를 받게 되는 도시의 총 개수는 몇개이며 도시들이 모두 메시지를 받는데까지 걸리는 시간은 얼마인가?
#N과 M의 크기가 충분히 크므로 앞서 다루었던 우선순위 큐를 이용한 다익스트라 알고리즘의 소스코드에서 마지막 부분만 조금 수정하여 코드를 만든다.
import heapq
import sys
imput=sys.stdin.readline
INF=int(1e9)
n,m,start=map(int,input().split())
graph=[[]for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    x,y,z=map(int,input().split())  #모든 간선 정보를 입력받는다. x번 노드에서 y노드로 가는 비용이 z라는 의미
    graph[x].append((y,z))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    distance[start]=0
    while q: #큐가 비어있지 않다면
        dist, now=heapq.heappop(q) #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now]<dist:
            continue  #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        for i in graph[now]:
            cost=dist+i[1] #현재 노드와 연결된 다른 인접한 노드들을 확인
            if cost<distance[i[0]]: #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0])) 


dijkstra(start)

count=0 #도달할 수 있는 노드의 개수
max_distance=0 #도달할 수 있는 노드중에서, 가장 멀리 있는 노드와의 최단 거리
for d in distance:
    if d!=INF:
        count+=1
        max_distance=max(max_distance,d)

print(count-1,max_distance)


