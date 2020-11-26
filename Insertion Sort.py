#시간 복잡도:O(n^2)
#특정한 데이터를 적절한 위치에 삽입하는 정렬. 
# 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
array=[7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)): #첫번째 데이터는 그 자체로 정렬되어 있다고 생각하고 두번째 데이터부터
    for j in range(i,0,-1):   #i부터 1까지 1개씩 감소한다.
        if array[j]<array[j-1]:  
            array[j],array[j-1]=array[j-1],array[j]    #한칸씩 왼쪽으로 이동
        else:
            break

print(array)
