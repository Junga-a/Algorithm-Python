#간단한 다익스트라 알고리즘 소스코드
#시간복잡도 O(V^2)
import sys
input=sys.stdin.readline
INF=int(1e9) #무한을 의미하는 값으로 10억 삽입
n,m=map(int,input().split())
start=int(input())
graph=[[]for i in range(n+1)]
visited=[False]*(n+1)
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())  #모든 간선 정보를 입력받는다. a번 노드에서 b노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))
    
def get_smallest_node():  #방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
    min_value=INF
    index=0
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index

def dijkstra(start):
    distance[start]=0
    visited[start]=0
    for j in graph[start]:
        distance[j[0]]=j[1]
    for i in range(n-1): #시작 노드를 제외한 전체 n-1개의 노드에서 반복
        now=get_smallest_node()
        visited[now]=True  #현재 최단거리가 가장 짧은 노드를 찾아서 방문 처리
        for j in graph[now]:
            cost=distance[now]+j[1] #현재 노드와 연결된 다른 노드를 확인하여 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[j[0]]:
                distance[j[0]]=cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])