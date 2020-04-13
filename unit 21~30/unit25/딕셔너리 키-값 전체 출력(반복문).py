x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i,end=' ')

# 딕셔너리와 for문을 활용한 모든 키 값 출력하기
# 키와 값을 모두 출력하기 위해서는 for in 뒤에 딕셔너리를 지정한 뒤 items를 사용해야 함
# for 키,값 in 딕셔너리.items() :
#    반복할 코드



x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items(): # items자리 대신 keys() , values() 도 사용가능
    print(key, value)




keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)

# 딕셔너리 표현식



x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
 
for key, value in x.items():
    if value == 20:    # 값이 20이면
        del x[key]     # 키-값 쌍 삭제
 
print(x)
# 딕셔너리 표현식에서 if문 사용



x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy()

# 딕셔너리 복사도 리스트와 마찬가지로 깊은 복사를 해야 함
