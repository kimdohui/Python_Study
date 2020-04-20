class Counter:
    def __init__(self, stop):
        self.stop = stop
 
    def __getitem__(self, index): # getitem사용 시 __iter__과 __next__ 생략 가능
        if index < self.stop:
            return index  # 인덱스 반환됨
        else:
            raise IndexError
 
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])
 
for i in Counter(3):
    print(i, end=' ')


# __getitem__ 메서드를 구현하여 인덱스로 접근 가능한 이터레이터


print('\n--------------\n')

import random

for i in iter(lambda : random.randint(0,5), 2)  # 0~5 사이의 난수를 생성하되 2가 나오면 종료
    print(i, end=' ')



print('\n--------------\n')

it = iter(range(2))

print(next(it, 10)) # next에 기본 값 설정 시 반복이 끝나도 stopIteration 발생이 아닌 기본값을 출력함
print(next(it, 10)) # 0
print(next(it, 10)) # 1
print(next(it, 10)) # 10
print(next(it, 10)) # 10
