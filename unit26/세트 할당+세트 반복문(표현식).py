a = {1, 2, 3, 4}
b = a

# 세트의 얕은 복사 (a와b는 같은 객체)
# b에 요소 변경 시 a와b 모두 적용 됨


a = {1, 2, 3, 4}
b = a.copy()

# 깊은 복사 (이로써 a b 모두 분리됨)


print('------------')
a = {1, 2, 3, 4}
for i in a :
    print(i)

# for문으로 a 요소 전체 출력하기



print('------------')
a = {i for i in 'pen'} # in 뒤에 문자열을 문자로 나누어 세트를 만든 뒤 a에 저장
print(a)
# {'n', 'p', 'e'}

a = {i for i in 'pineapple' if i not in 'apl'} # 위와 동일한 구조지만 if문을 사용해 apl은 세트에서 제거
print(a)
#{'e', 'i', 'n'}



