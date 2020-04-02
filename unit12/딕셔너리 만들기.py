lux = [500,300,200]

# 게임 스탯을 담은 리스트 lux에서 각각 무엇을 말하는지 알기 힘들다

lux = {'health':500, 'mana' : 300, 'melee':200}
print(lux)

# 이런식으로 딕셔너리를 활용하면 값마다 이름이 붙어서 한눈에 알아보기가 좋다.
# 딕셔너리 키에는 값을 하나만 지정할 수 있다.


print(' ')
lux = {'health':500, 'health' : 300, 'melee':200}
print(lux) # 'health' : 300

# 이렇듯 키 이름이 중복되면 가장 뒤에 값이 사용된다.(중복키는 저장되지 않는다.)


print(' ')
x = {100:'hundred' , False : 0 , 3.2 : [3.5]}
print(x)

# 딕셔너리의 키는 문자열뿐 아니라 정수,실수,불을 사용할 수 있으며 자료형을 섞어서 사용해도 된다
# 딕셔너리의 값에는 모든 자료형을 쓸 수 있다.(list 등)

print(' ')
x = {}
print(x)
y = dict()
print(y)

# 빈 딕셔너리 만들기


print(' ')
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)  # 키 = 값 형식으로 만듬
print(lux1)

# 이렇게 dict로 딕셔너리를 만들 수 있다. 이땐 키에 ' 나 "를 쓰면 안된다.(키는 문자열로 변함)



print(' ')
x = dict(zip(['mana' , 'hp'], [100,200])) # zip함수
print(x)

# zip 사용하여 딕셔너리 만들기




print(' ')
x = dict([('hp',100), ('mana' , 400)])
print(x)

# 튜플에 저장해 zip안에 넣어 딕셔너리 생



print(' ')
x = dict({'hp':100, 'mana':300})
print(x)

# dict안에 중괄호로 딕셔너리 생성
