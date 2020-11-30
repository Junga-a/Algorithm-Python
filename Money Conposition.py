#N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다. 
# 사용한 화폐의 구성은 같지만 순서만 다른것은 같은 경우로 구분한다. 첫째 줄에 N,M을 출력받고 이후 N개의 줄에는 각 화폐의 가치가 주어진다.
#결과는 M원을 만들기 위한 최소한의 화폐 개수를 출력하고, 불가능 할때는 -1을 출력한다.
#a(i)는 금액 i를 만들기 위한 최소한의 화폐개수, 화폐의 단위를 k라고 하면 a(i-k)를 만드는 방법이 존재하는 경우 a(i)=min(a(i),a(i-k)+1)
#a(i-k)를 만드는 방법이 없으면 a(i)=10001(무작정 큰 수 아무거나)
n,m=map(int,input().split())
array=[]
for i in range(n):
    array.append(int(input()))

d=[10001]*(m+1)  #0부터 m까지 넣으려면 m+1

d[0]=0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]]!=10001:  #(i-k)원을 만드는 방법이 존재하는 경우
            d[j]=min(d[j],d[j-array[i]]+1)

if d[m]==10001:
    print(-1)
else:
    print(d[m])