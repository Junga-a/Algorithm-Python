#이진 탐색은 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 과정이다.
#시간 복잡도는 O(logN)으로 매우 작다..
def binary_search(array, target, start, end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        return mid #찾은 경우 중간점 인덱스 반환
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1) #중간점의 잢보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    else:
        return binary_search(array, target,mid+1,end)

n, target=map(int, input().split())
array=list(map(int, input().split()))

result=binary_search(array, target, 0, n-1)
if result==None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

