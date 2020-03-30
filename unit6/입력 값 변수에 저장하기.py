x = input('문자열을 입력하세요 : ')
print(x)

# 입력을 받을 땐 input() 사용 / 변수에 input( )를 담고 변수를 출력하면 입력결과가 나옴

print(' ')
a = input('첫번째 수 : ')
b = input('두번째 수 : ')
c = int(a) + int(b)
print(a+b)
print(c)
print(type(a))
print(type(b))

# 입력받는 수는 기본적으로 문자열 형태라 우리가 원하는 값인 a+b가 아니라 ab 가 나옴
# 정수의 합을 구하고 싶은 거라면 int() 형태로 형변환 한 뒤 출력해야 함

print(' ')
print(' ')
a,b = input('값 2개 입력 : ').split()
print(a)
print(b)
c = int(a)+int(b)
print(c)
#split은 분리하다라는 뜻으로 입력받은 값을 공백을 기준으로 분리해 변수에 차례대로 저장함
# 정수의 합을 구하고 싶은 거라면 int() 형태로 형변환 한 뒤 출력해야 함


print(' ')
a,b = map(int, input('숫자 2개 입력 : ').split())
print(a+b)

#위와 같이 map을 사용하면 입력값의 형을 따로 바꾸지 않아도 됨

print(' ')
x, y = map(int, input('숫자 두 개를 입력하세요: ').split(',')) 
print(x + y)

