a = [[10, 20], [30, 40]]
b = a
b[0][0] = 100
print(a)
print(b)

# 2차원 리스트를 만든 뒤 다른 변수에 할당하고 요소 변경 시 두 리스트에 모두 반영


print('\n--------  2\n')
a = [[10, 20], [30, 40]]
import copy
b = copy.deepcopy(a)
b[0][0] = 100
print(a)
print(b)

# copy 모듈의 deepcopy를 사용해 깊은 복사를 함(a와 b가 가르키는 리스트가 다름)


