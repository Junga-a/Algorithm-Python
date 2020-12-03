#공통 원소가 없는 두 집합, 트리 자료구조를 이용하여 집합을 표현하는데 알고리즘은 다음과 같다.
#1.union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A,B를 확인한다. A와 B의 루트 노드 A',B'를 찾는다. A'를 B'의 부모 노드로 설정한다. 
# 2. 모든 union연산을 처리할때까지 1의 과정을 반복한다.
def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x]) #특정 원소가 속한 집합을 찾아서, 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    return x

def union_parent(parent,a,b): #두 원소가 속한 집합을 합치기
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split()) #노드의 개수와 간선의 개수
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i #부모 테이블 상에서 부모를 자기 자신으로 초기화

for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

print('각 원소가 속한 집합: ',end=' ')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()

print('부모 테이블: ',end=' ')
for i in range(1,v+1):
    print(parent[i],end=' ')
