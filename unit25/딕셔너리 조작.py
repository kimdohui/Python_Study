x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e') # 키만 지정해서 값에 None 저장
x.setdefault('f', 100)  # 키와 기본 값 저장
print(x)

# 딕셔너리에 키 값 추가


print('\n-------------  2\n')
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=50)  # 만약 해당 키가 없으면 키-값 쌍을 추가함(키=값 형식은 키가 문자열일때만 사용가능)
print(x)

# 딕셔너리 값 수정
# 키가 숫자라면 update(딕셔너리) 형식으로 넣을 수 있음 update({1:'0ne'})


print('\n-------------  3\n')
y = {1: 'one', 2: 'two'}
y.update([[2, 'TWO'], [4, 'FOUR']])
print(y)

# 리스트와 튜플로 값 수정하기
#  y.update(zip([1, 2], ['one', 'two']))과 같이 zip 객체로 값을 수정할 수 있음


print('\n-------------  4\n')
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')  # del x['a']와 같음
print(x)

# 딕셔너리 값 삭제


print('\n-------------  5\n')
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem()
print(x)

 # 딕셔너리 임의의 값 삭제(파이썬 3.6 이상에서는 마지막 키-값을 삭제)

print('\n-------------  6\n')
x.clear()
print(x)

# 딕셔너리 모든 키-값 삭제


print('\n-------------  7\n')
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('a'))  # 원하는 키 값 가져오기
print(x.items())  # 모든 키 값 가져오기



print('\n-------------  8\n')
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys) # 키리스트(keys) 뒤에 값 지정 시 키의 값으로 대체fromkeys(keys,100)
print(x)

# 리스트 딕셔너리 만들기(튜플도 동일)
