#수열을 내림차순으로 정렬하는 프로그램을 만드시오.
#입력조건:첫쨰 줄에 수열에 속해 있는 수의 개수 N이 주어진다.(1<=N<=500)
#입력조건: 둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다. 수의 범위는 1 이상 100000이하의 자연수이다.
#출력조건: 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는 자유롭게 출력해도 괜찮다.

n=int(input())

array=[]
for i in range(n):
    array.append(int(input()))

array=sorted(array,reverse=True)

for i in array:
    print (i, end=' ')