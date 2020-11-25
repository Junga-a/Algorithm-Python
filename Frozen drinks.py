# N X M 크기의 얼음틀이 있다. 구명이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상,하,좌,우로 
# 붙어있는 경우서로 연결되어 있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 떄 생성되는 아이스크림의 개수를 구해라.
#1.dfs를 이용하여 구할 수 있다. 특정한 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에서 값이 0이면서 아직 방문하지 않은 지점을 방문한다.
#2.방문한 지점에서 다시 상,하,좌,우를 살펴보면서 연결된 모든 지점을 방문한다.
#3. 1~2번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다.
n,m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False #주어진 범위를 벗어나는 경우에는 즉시 종료
    if graph[x][y]==0:
        graph[x][y]=1
        #상,하,좌,우 함수 호출하되 재귀로 호출해서 스택에 쌓이게함
        #DFS 1번 할 때마다 연결된 얼음이 다 얼어서 얼음 개수는 DFS 1번 할 때마다 1씩 증가
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

#모든 노드에 대하여 음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result +=1

print(result)
