def hello():
    print('hello')

hello()

# 함수 만들기

print('\n------------------\n')

def add(a,b):
    """독스트링""" # 독스트링을 사용하면 함수에 대한 설명을 넣을 수 있음
    print(a+b)

add(10,20)

# 덧셈 함수 만들기


def add(a,b):
    return a+b

a = add(10,20)
print(a)
print(add(10,20)) # 이런 식으로 바로 출력할 수 있음

# 덧셈 함수 변수에 대입하기



print('\n------------------\n')
def add(a,b):
    return a+b,a-b

a,b = (add(10,20)) # 만약 반환값이 여러 개일때 변수가 1개인 경우(30,-10)같이 튜플이 반환된다

print(a)
print(b)

# return 값 여러개 반환하기


# 함수는 스택방식으로 호출 됨
