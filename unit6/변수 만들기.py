x = 10
print(x)
y = 'Hello world'
print(y)

# 변수 선언 후 숫자, 문자열  출력하기

print(' ')
print(type(x))
print(type(y))

# type으로 변수의 자료형을 알아 낼 수 있음

print(' ' )
x,y,z = 10,20,30
print(x,y,z)

#파이썬 에서는 변수 여러 개를 한 번에 만들 수 있음(단 변수 개수와 값의 수가  동일 해야 함)

print(' ')
x=y=z = 10
print(x,y,z)

#만약 같은 값을 가진 변수를 만든다면 x=y=z=값 또는 x,y,z = 값,값,값 같이 써주면 됨


print(' ')
x,y = 10, 20
print(x,y)
x,y = y,x
print(x,y)

#위와 같이 써주면 변수의 값을 서로 바꿀 수 있음

print(' ')
x= 10
print(x)
del x
print(x)

#del은 변수를 삭제할 때 사용함

print(' ')
x = None
print(x)

# 변수에 None을 집어넣으면 값이 들어있지 않은 빈 변수가 된다.( = null )
