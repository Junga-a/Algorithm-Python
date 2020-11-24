# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려 한다. 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

n,k=map(int,input().split())
result=0

while True:
    target=(n//k)*k #target은 K와 가장 가까운 K로 나누어 떨어지는 수
    result+=(n-target) #1을 뺴는 연산횟수를 더함
    n=target
    if n<k:
        break
    result+=1
    n//=k

result+=(n-1) #n이 1보다 크다면 1을 빼는 연산
print(result)