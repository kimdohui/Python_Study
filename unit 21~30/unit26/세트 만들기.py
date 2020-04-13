fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)

# 세트 만들기 (세트에 들어가는 요소는 중복될 수 없음)
# 세트는 리스트,튜플,딕셔너리와 달리 []로 특정 요소만 출력할 수 는 업ㅄ다


print('grape' in fruits) # in 앞에  not 이 붙으면 특정 값이 없는지 확인

# 세트에 특정 값이 있는 지 확인하기(있으면 True 반환)



a = set('apple') # range(범위) 같이 사용할 경우 0~범위 에 해당하는 숫자를 가진 세트를 만들 수 있음
print(a)
print(type(a))

# a 에 들은 문자들로 세트가 만들어짐(set뒤에 아무것도 넣지 않으면 빈 세트를 만듬)
# type 사용 시 자료형의 종류를 알 수 있음(여기는 세트)


# 세트는 세트안에 세트를 넣을 수 없음

# frozenset 사용 시 변경할 수 없는 세트를 제공함






