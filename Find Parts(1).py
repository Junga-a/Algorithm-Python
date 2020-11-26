#동빈이네 전자매장에는 부품이 N개가 있다. 어느날 순님이 M개 종류의 부품을 대량으로 구매하겠다고 견적서를 보냈다. 
# 이때 가게 안에서 부품이 모두 있는지 확인해보자. 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes, 없으면 no를 출력한다.
#이진탐색 법으로 푸는법

def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

n=int(input())
array=list(map(int, input().split()))
array.sort()
m=int(input())
x=list(map(int, input().split()))

for i in x:
    result=binary_search(array, i, 0, n-1)
    if result!=None:
        print("yes",end=' ')
    else:
         print("no",end=' ')