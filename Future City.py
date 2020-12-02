#방문 판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다. 
# 연결된 2개의 회사는 양방향으로 이동할 수 있으며, 특정 회사와 다른 회사가 도로로 연결되어 있다면 정확히 1만큼의 시간으로 이동할 수 있다. 
# 소개팅 상대는 K번에 위치할 때, 방문 판매원 A는 1번회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표다. 
# 이 때 최소시간을 계산하는 프로그램을 작성하시오
INF=int(1e9)

n,m=map(int, input().split())

graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1  #a와b가 서로에게 가는 비용은 1이라고 산정

x,k=map(int,input().split())
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

distance=graph[1][k]+graph[k][x]


if distanve>=INF:
    print("-1")
else:
    print(distance)
