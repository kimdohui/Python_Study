def cal() :
    a = 3
    b = 5
    def add_num(x) :
        return a*x+b  # 함수 바깥 지역 변수를 사용하여 계산
    return add_num  # add 함수 자체를 반환(괄호를 쓰지 않는다)

c = cal() # add_num을 반환했는데도 불구하고 c는 cal의 지역변수 a,b를 사용해 계산함
print(c(1), c(2), c(3), c(4), c(5))


# 이렇게 함수를 둘러싼 환경을 유지하다가 함수를 호출할 때 다시 꺼내서 사용하는 함수를 클로저라 함
# 여기서는 c에 저장된 함수가 클로저임


# 클로저를 사용하면 프로그램의  흐름을 변수에 저장할 수 있음
# 즉 클로저는 지역 변수와 코드를 묶어서 사용하고 싶을 때 활용함
# 또한 클로저에 속한 지역 변수는 바깥에서 직접 접근할 수 없으므로 데이터를 숨기고 싶을 때 활용


print('\n-------------\n')

# lambda로 클로저 만들기

def calc():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환
 
c = calc()
print(c(1), c(2), c(3), c(4), c(5))



print('\n-------------\n')

# 클로저의 지역 변수 변경하기

def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
 
c = calc()
c(1)  # 8
c(2)  # 19
c(3)  # 33


#클로저의 지역 변수를 변경하고 싶다면 nonlocal을 사용하면 됨
