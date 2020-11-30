#한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법
#메모이제이션 기법을 사용한 피보나치 수열 구하기
d=[0]*100

def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]  #이미 계산한 적 있는 문제라면 그대로 반환
    d[x]=fibo(x-1)+fibo(x-2) #아직 계싼하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    return d[x]

print(fibo(99))