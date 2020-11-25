#재귀 함수를 이용한 팩토리얼 예제
def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)

print('재귀적으로 구현:', factorial_recursive(5))
