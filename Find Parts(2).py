#계수정렬 법으로 푸는법
n=int(input())
array=[0]*1000001

for i in input().split():
    array[int(i)]=1            #가게에 있는 전체 부품 번호를 입력받아서 기록, array(8)=1이고 array(3)=1이면 array[i]==1이면 yes

m=int(input())
x=list(map(int, input().split()))

for i in x:
    if array[i]==1:
         print("yes",end=' ')
    else:
         print("no",end=' ')




