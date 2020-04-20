it = [1, 2, 3].__iter__()  # 리스트의 이터레이터를 변수에 저장
print(it.__next__())  # __next__ 메서드를 차례대로 호출
print(it.__next__())
print(it.__next__())

# 요소를 차례대로 꺼낼 수 있음




class Counter:
    def __init__(self, stop):
        self.current = 0    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop    # 반복을 끝낼 숫자
 
    def __iter__(self):
        return self         # 현재 인스턴스를 반환
 
    def __next__(self):
        if self.current < self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current            # 반환할 숫자를 변수에 저장
            self.current += 1           # 현재 숫자를 1 증가시킴
            return r                    # 숫자를 반환
        else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration         # 예외 발생
 
for i in Counter(3):
    print(i, end=' ')  # 0 1 2


# 이터레이터 만들기

a,b,c = Counter(3)
print(a,b,c)

a,b,_,d = Counter(4)  # 여기서 _는 특장 값을 사용하지 않고 무시하겠다는 뜻이다
print(a,b,d) # a,b,d만 사용하기 때문에 _로 대체한 것이다.

# 이때 이터레이터는 언패킹이 가능함


