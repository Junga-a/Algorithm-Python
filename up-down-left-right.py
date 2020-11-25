# 여행가 A는 N X N크기의 정사각형 공간 위에 서있다. 가장 왼쪽 위 자표는 (1,1)이며 오른쪽 아래 좌표는 (N,N)에 해당한다. 시작좌표는 항상 (1X1)이다.
# L:왼쪽으로 한 칸 이동, R:오른쪽으로 한 칸 이동, U:위로 한 칸 이동, D:아래로 한 칸 이동, 정사각형 공간을 벗어나려는 움직임은 무시된다.
# 입력조건: 첫째 줄에 공간의 크기를 나타내는 N이 주어진다(1<=N<=100)
# 입력조건: 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다(1<=이동횟수<=100)
# 출력조건: 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X, Y)를 공백으로 구분하여 출력한다.
n=int(input())
x,y=1,1
plans=input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D'] #L은 y좌표-1, R은 y좌표 +1, U는 x좌표 -1, D는 x좌표 +1

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]

    if nx<1 or ny<1 or nx>n or ny>n: #공간을 벗어나는 경우 무시하기
        continue
    x,y=nx,ny

print(x,y)