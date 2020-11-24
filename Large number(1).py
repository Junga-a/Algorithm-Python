#하나의 배열을 입력받아, 주어진 수들을 M번 더하여 가장 큰 수를 만다는 법칙이다. 
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
#입력조건:첫째 줄에 N(2<=N<=1000),M(1<=M<=10000),K(1<=K<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
#입력조건:둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10000이하의 수로 주어진다
#입력조건:입력으로 주어지는 K는 항상 M보다 작거나 같다.
#출력조건:첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 값을 출력한다.
n,m,k=map(int,input().split())
data=list(map(int, input().split()))

data.sort() #오름차순 정렬, 작은수부터 큰수로
first=data[n-1]
second=data[n-2]

result=0

while True:
    for i in range(k): 
        if m==0: #가장 큰 수를 k번 더하고, 그럴때마다 m-1, m==0이면 탈출
            break
        result+=first
        m-=1 
    if m==0: #두번째로 큰 수를 k번 더하고, 그럴때마다 m-1, m==0이면 탈출
        break
    result+=second
    m-=1


print(result)