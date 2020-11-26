#집합 자료형 이용해서 푸는법
n=int(input())
array=set(list(map(int, input().split())))
m=int(input())
x=list(map(int, input().split()))

for i in x:
    if i in array:
        print("yes",end=' ')
    else:
         print("no",end=' ')