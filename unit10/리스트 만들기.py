a = [1,2,3,4,5]
print(a)
b = ['hana' , 7 , True]
print(b)
# 리스트 생성 / 이때 리스트 안에 저장된 값을 요소라 부름
# 리스트의 장점 : 문자열, 정수, 실수 , 불 등 자료형에 상관없이 하나의 리스트에 저장해도 됨


print(' ')
a = []
print(a)
b = list()
print(b)

# 빈 리스트 만들기


print(' ')
print(range(5))      # range(0, 10)
a = list(range(5))
print(a)

# range는 연속된 숫자를 생성하는데 예를 들어 5를 지정하면 0부터 4까지 숫자를 생성한다.
# 이때 range로 지정한 숫자는 생성 숫자에 포함되지 않는다.(5 출력 X)


print(' ')
a = list(range(5,10))
print(a)

# range로 시작하는 숫자와 끝나는 숫자를 지정할 수 있는데 이때도 끝 숫자는 포함하지 않는다.( (5,10)이면 5~9 )

print(' ')
a = list(range(-10,0,2))  # [-10, -8, -6 , -4 , -2] 
print(a)
a = list(range(10,0,-1))
print(a)

# 세 번째 자리에 증가폭을 사용할 수 있다.


