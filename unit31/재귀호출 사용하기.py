#def hello() :
#    print('hello')
#    hello()
#
#hello()


# 재귀 호출 사용(함수 안에서 자기자신을 호출하는 방식)

def hello(num) :
    if num == 0:
        return

    print('hello',num)

    num -= 1
    hello(num)

hello(10)


# 재귀호출 종료 조건 만들기

print('\n-------\n')
def factorial(n) :
    if n == 1 :
        return 1
    return (n * factorial(n-1))

print(factorial(4)) # 24

# 팩토리얼을 재귀함수로 만들기


