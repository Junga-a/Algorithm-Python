#sorted()함수는 시간 복잡도 O(NlogN)을 보장하는 병합정렬을 기반으로 만들어졌다.
#1.
array=[7,5,9,0,3,1,6,2,4,8]
result=sorted(array)
print(result)

#2.
array.sort()
print(array)

#3.
array=[('바나나',2),('사과',5),('당근',3)]
def setting(data):
    return data[1]
result=sorted(array,key=setting)
print(result)