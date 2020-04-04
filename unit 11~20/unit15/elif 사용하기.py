x = 10
if x == 10:
    print('10이다')
elif x == 20 :
    print('20이다.')

# elif 는 else if 라는 뜻이다. elif는 단독으로 사용할 수 없다.

print(' ')
x = 10

if x == 5 :
    print('x는 5이다.')
elif x == 10 :
    print('x는 10이다.')
else :
    print('5도 아니고 10도 아니다.')

# 이렇게 하면 if , elif의 조건문이 모두 거짓일 때만 else의 코드가 실행된다.
# elif는 else, if와 다르게 여러 번 사용할 수 있고 elif 앞에 else가 오면 잘못된 문법이 된다.

print(' ')
# 자판기 만들기

button = int(input())

if button == 1:
    print('사이다')
elif button == 2 :
    print('콜라')
elif button == 3 :
    print('코코팜')
else :
    print('제공하지 않는 메뉴')
    
