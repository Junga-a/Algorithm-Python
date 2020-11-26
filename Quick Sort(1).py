#시간 복잡도:O(NlogN)
# 큰숫자와 작은 숫자를 교환할 때, 교환하기 위한 기준을 피벗이라고 한다.
#피벗카드 기준으로 오른쪽으로 자기보다 큰 데이터를, 왼쪽으로 자기보다 작은 데이터를 찾아 두 위치를 서로 변경한다.
#리스트를 피벗 기준으로 두개로 나누어서 각자 또 기준 피벗을 정해 오른쪽으로 자기보다 큰 데이터를, 왼쪽으로 자기보다 작은 데이터를 찾아 두 위치를 서로 변경한다.
#현재 리스트의 원소가 1개라면, 퀵정렬을 종료한다.

array=[5,7,9,0,3,1,6,2,4,8]
def quick_sort(array,start,end):
    if start>=end:
        return  #원소가 1개인 경우 종료
    pivot=start #피벗은 첫번째 원소
    left=start+1
    right=end
    while left<=right: 
        while left<=end and array[left]<=array[pivot]: #피벗보다 큰 데이터를 찾을 때까지 반복
            left+=1
        while right>start and array[right]>=array[pivot]:  #피벗보다 작은 데이터를 찾을 때까지 반복
             right-=1
        if left>right: #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[left],array[right]=array[right],array[left] #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)