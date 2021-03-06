x = {'hp' :100, 'mana' : 200}
print(x['mana'])
print(x)

# 딕셔너리 키에 접근할 때에는 딕셔너리 위에 [ ] 를 붙여 사용하고 이 안에 키를 지정해주면 된다.
# 딕셔너리에 키를 지정하지 않으면 딕셔너리 전체를 출력한다.


print(' ')
x = {'hp' :100, 'mana' : 202}
x['hp'] = 1002
print(x)

# 딕셔너리는 []로 키에 접근한 뒤 값을 할당한다.


print(' ')
x = {'hp' :100, 'mana' : 200}
x['speed'] = 10
print(x)

# 만약 딕셔너리에 없는 키에 값을 할당하면 해당 키가 추가되고 값이 할당 된다.
# 존재하지 않는 키에서 값을 가져오려 하면 에러가 발생함


print(' ')
x = {'hp' :100, 'mana' : 200}
print('hp' in x)
print('hp' not in x)

# 딕셔너리에 키가 있는지 확인하고 싶다면 in 연산자를 사용하면 된다.
# in 앞에 not을 붙이면 키가 없는지 확인함(값이 없다면 True 반환)


print(' ')
x = {'hp' :100, 'mana' : 200}
print(len(x))

# len을 활용하면 딕셔너리의 키 개수를 구할 수 있다.
