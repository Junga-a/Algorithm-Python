#N개의 원소로 구성된 두 배열에서, 동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 
# 동빈이의 최종목표는 배열 A의 모든 원소의 값이 최대가 되도록 하는 것이다.
#문제 해설:매번 A배열에서 가장 작은 원소를 골라서, B에서 가장 큰 원소와 교체한다.
n,k=map(int, input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort() #배열 A 오름차순 정렬
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break

print(sum(a))