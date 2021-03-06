# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려 한다. 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

n,k=map(int,input().split())
result=0

# N이 K 이상이라면 K로 계속 나누기
while n>=k:
    while n%k!=0:
        n-=1
        result+=1
    n//=k
    result+=1

# 마지막으로 남은 n이 2, k가 3이거나 n이 4, k가 5이면 즉, n이 1보다 크면 1이 될때까지 n을 1개씩 빼주고 result에 1씩 더해준다.
while n>1:
    n-=1
    result+=1

print(result)