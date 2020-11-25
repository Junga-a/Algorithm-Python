#행복 왕국의 왕실 정원은 체스팔과 같은 8X8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서 있다. 
# 나이트는 말을 타고 있기 때문에 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다. 나이트는 특정한 위치에서 2가지 경우로만 이동한다.
#1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
#2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
#행위치는 1부터8로, 열위치는 a부터h로 표현한다.
#나이트가 이동할 수 있는 경우의 수를 출력하시오.

input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0]))-int(ord('a'))+1 #ord는 문자의 아스키 코드 값을 돌려주는 함수이다.(chr과 반대) 몇번째 알파벳인지를 정해준다.
                                                #c(99)-a(97)+1=3번째 알파벳, 컬럼값

steps=[(-2,-1),(-2,1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)] #나이트가 이동할 수 있는 8가지 방향 정의

result=0
for step in steps:
    next_row=row+step[0]
    next_column=column+step[1]
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result+=1

print(result)