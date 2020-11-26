#떡볶이의 떡을 자를때, 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춘다. 높이(H)를 설정하면 H보다 긴 떡은 잘리고, 짧은 떡은 안잘린다.
#손님은 긴 떡을 잘랐을때의 나머지(꼬랑지)를 가져간다.
#손님이 왔을 때 요청한 총 길이가 M일때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최대값을 구하시오.
n,m=list(map(int, input().split()))
array=list(map(int, input().split()))

start=0
end=max(array)

result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    for x in array:
        if x>mid:
            total+=x-mid #잘랐을때의 떡의 양 계산
    if total<m:    
        end=mid-1 #떡의 양이 부족한 경우 더 많이 자르기
    else:
        result=mid #최대한 덜 잘랐을떄가 정답이므로, 일단 여기에서 result에 기록(start>end될때까지 계속 갱신)
        start=mid+1  #떡의 양이 충분한 경우 덜 자르기

print(result)