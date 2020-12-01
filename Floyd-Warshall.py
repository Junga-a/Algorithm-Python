#플로이드 워셜 알고리즘은 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용할 수 있는 알고리즘이다.
#각 단계마다 특정한 노드 k를 거쳐 가는 경우를 확인한다. a에서 b로 가는 최단거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사합니다. 
# D(ab)=min(D(ab),D(ak)+D(kb))
INF=int(1e9)
n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)] #2차원 리스트(그래프 표현)을 만들고 모든 값을 무한으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0 #자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c #각 간선에 대한 정보를 입력받아, 그 값으로 초기화

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b]) #점화식에 따라 플로이드 워셜 알고리즘을 수행

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINITY",end=" ")
        else:
            print(graph[a][b],end=" ")
    print()

