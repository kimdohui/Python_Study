x = 10

if x == 0 :
    print('x는 0이다')

else :
    print('x는 0이 아니다')

# else는 if문이 참이 아닐 경우 실행한다.


print(' ')
x = 10
y = 'x는 0이다' if x == 0 else 'x는 0이 아니다'
print(y)

# 위와 같은 문장을 변수 = 값 if 조건문 else 값 형식으로 단축한 것이다.
# else 또한 if와 마찬가지로 여러 줄일때 마지막 줄의 들여쓰기를 하지 않으면 의도하지 않은 동작이 된다.

print(' ')
if True :
    print('참')
else :
    print('거짓')

if None :
    print('참')
else :
    print('거짓')

# True는 if의 코드가 실행되고 False는 else의 코드가 실행된다.(None은 false로 취급)


print(' ')
if 0 :
    print('참')
else :
    print('거짓')

if 0x1F : # 16진수
    print('참')
else :
    print('거짓')

# 숫자는 정수(2,10,16 진수) , 실수와 관계없이 0이면 거짓, 0이 아닌 수는 참이 된다.


print(' ')
if 'Hi':    # 문자열
    print('참')    # 문자열은 참
else:
    print('거짓')
 
if '':    # 빈 문자열
    print('참')
else:
    print('거짓')    # 빈 문자열은 거짓

# 문자열은 내용이 있으면 참, 비어있으면 거짓이 된다.


print(' ')
if not 0 :
    print('참')

# 이와 같이 0,None, '' 에 앞에 not을 붙이면 참이 된다.
