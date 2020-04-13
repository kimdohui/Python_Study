a = [1,2,3,4,5,6]
b = list(map(lambda x:str(x) if x%3==0 else x,a))
print(b)

# 3의 배수들만 문자열로 출력하기(조건부 표현식 구조는  식1 if 조건식 else 식2 이다.)
# 위와 알아보기 힘든 람다식들은 함수로 쓰는 것을 권장함

def f(x) :
    if x%3 == 0:
        return str(x)
    else:
        return x

# 람다 표현식에서 if를 사용했다면 반드시 else를 사용해야 함(elif 사용 금지)


print('\n------------\n')
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]

print(list(filter(lambda x: x > 5 and x < 10, a)))

# 람다 표현식을 filter에 넣기


print('\n------------\n')
a = [1,2,3,4,5]
from functools import reduce

print(reduce(lambda x,y:x+y,a))

# reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전결과와 누적해 반환하는 함수이다.


# 람다 표현식을 reduce에 넣기

