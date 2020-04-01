a = (1,2,3)
print(a)
b = (1)
c = (1,) # (1, ) == 1,
print(b,c)

# 튜플은 (괄호)를 사용해서 만들며 요소를 변경할 수 없도록 만든다.
# 튜플을 1개만 넣을 때에는 괄호 안 숫자 옆에 쉼표를 찍거나 쉼표를 찍은 숫자를 변수에 넣어준다.(안그러면 튜플이 아닌 그냥 수로 인식)

print(' ')
a = ('hana' , 15)
print(a)

# 튜플도 리스트처럼 여러 자료형을 섞어서 저장해도 된다.


print(' ')
a = tuple(range(10))
b = tuple(range(5,10))
c = tuple(range(5,10,2))
print(a)

# range를 사용하여 튜플 만들기와 증가폭 지정하


print(' ')
a = [1,2,3]
print(tuple(a))
b = (1,2,3)
print(list(b))

#튜플을 리스트로 , 리스트를 튜플로 만들기

print(' ')
print(list('hello'))
print(tuple('hello'))

# list와 tuple에 만자열을 넣으면 문자 리스트, 문자 튜플이 생성된다.

print(' ')
a,b,c = [1,2,3]
print(a,b,c)
d,e,f = (4,5,6)
print(d,e,f)

# 리스트와 튜플 사용 시 변수를 한번에 여러 개 만들 수 있다.(이때 변수와 리스트(튜플)의 요소 수는 같아야 함

print(' ')
x = [1,2,3]
a,s,d = x
print(a,s,d)

#리스트와 튜플 변수로도 변수 여러 개를 만들 수 있는데 리스트와 튜플의 요소를 변수 여러 개에 할당하는 것을 리스트 언패킹, 튜플 언패킹이라 함

