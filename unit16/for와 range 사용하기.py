for i in range(3) :
    print('hello')

# range안에 숫자를 집어넣고 for문에 사용해주면 지정한 숫자만큼 반복문을 수행한다.

print(' ')
for i in range(5) :
    print('hello', i)
    


print(' ')
for i in range(5,10) :
    print('hello', i)

# for문에 range 사용해보기


print(' ')
for i in range(0,10,2) :
    print('hello', i)

# for문에 range 증가폭 사용하기


print(' ')
for i in range(10,0,-1) :
    print('hello',i)

# for문 숫자 감소시키기



print(' ')
for i in reversed(range(10)) :
    print(i, end = ' ')           # 9 8 7 6 5 4 3 2 1 0
    i = 10  


# reversed를 사용하면 결과 값을 뒤집을 수 있다.(i=10을 할당하여 10을 출력할 것 같지만 i는 반복문이 진행될때마다 새로운 값으로 덮어써지기 때문에 영향을 주지 않는다.)



print('\n\n')
count= int(input('반복횟수 입력 : '))

for i in range(count) :
    print('hello', i+1,'번')


# 입력수만큼 반복하기


print(' ')
a = [1,2,3,4,5]
for i in a :
    print(i)
    

# for문에 range대신 리스트를 넣으면 리스트의 요소를 꺼내면서 반복함(튜플도 마찬가지)


print(' ')
animal = ('rabbit','cat')
for i in animal :
    print(i)

# 튜플 예시


print(' ')
for letter in 'hello':
    print(letter,end = ' ')

# 문자열도 하나씩 분리하여 출력할 수 있다.


print(' ')
for letter in reversed('hello'):
    print(letter,end = ' ')

# reversed 사용하여 거꾸로 출력함


