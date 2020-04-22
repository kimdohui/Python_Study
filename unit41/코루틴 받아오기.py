def add(a, b):
    c = a + b    # add 함수가 끝나면 변수와 계산식은 사라짐
    print(c)
    print('add 함수')
 
def calc():  # 메인루틴
    add(1, 2)    # add 함수가 끝나면 다시 calc 함수로 돌아옴 (서브루틴)
    print('calc 함수')
 
calc()


# 코루틴이란 서로 협력하는 루틴이란 뜻으로 메인루틴과 서브루틴이 대등한 관계이며
# 특정 시점에 상대방의 코드를 실행함

# 일반 함수 호출 시 코드를 한번만 실행할 수 있지만 코루틴은 여러번 실행 가능함




def number_coroutine():
    while True:        # 코루틴을 계속 유지하기 위해 무한 루프 사용
        x = (yield)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
        print(x)
 
co = number_coroutine()
next(co)      # 코루틴 안의 yield까지 코드 실행(최초 실행)
 
co.send(1)    # 코루틴에 숫자 1을 보냄
co.send(2)    # 코루틴에 숫자 2을 보냄
co.send(3)    # 코루틴에 숫자 3을 보냄
