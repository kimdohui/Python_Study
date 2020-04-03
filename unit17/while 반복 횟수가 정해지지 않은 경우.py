import random

print(random.random())

# 랜덤 수 출력하기


print(' ')
print(random.randint(1,5))
print(random.randint(1,5))

# 지정한 범위 내 난수 생성(위 같은 경우 1~5 사이에 난수를 생성한다.)


print(' ')

i = 0
while i != 2:
    i = random.randint(1,6)
    print(i)

# while문을 사용하여 2가 나올때까지 루프를 돌리게 설정함(while문은 반복횟수가 정해지지 않을 때 유용함)


animal = ['cat','dog','pig']
print(random.choice(animal))

# 시퀀스 객체에서 요소를 무작위로 선택할 수 있다.(리스트,튜플,range,문자열도 동일)


print(' ')
while True :
    print('hello, world')

# while 다음값이 True거나 True로 실행되는 값들(0이 아닌 숫자나 내용있는 문자열 등)은 무한루프를 발생
