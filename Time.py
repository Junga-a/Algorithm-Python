#정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

h=int(input())
count=0

for i in range(h+1): ##0부터 h까지, 0부터 59까지, 0부터 59까지 있는 모든 i,j,k중에 3이 포함 되면 count+1
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)