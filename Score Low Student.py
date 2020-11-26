#성적이 낮은 순서대로 학생의 이름을 출력하세요.
#입력조건: 첫번째 줄에 학생의 수 N이 입력된다.
#입력조건: 두번쨰 줄부터 N+1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다. 
#          문자열 A의 길이와 학생의 성적은 100이하의 자연수이다.
#출력조건: 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.
n=int(input())
array=[]
for i in range(n):
    input_data=input().split()
    array.append((input_data[0],int(input_data[1])))

def setting(data):
    return data[1]

array=sorted(array, key=setting)
for student in array:
    print(student[0],end=' ')