def sum_coroutine():
    total = 0
    while True:
        x = (yield total)    # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x
 
co = sum_coroutine()
print(next(co))      # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력
 
print(co.send(1))    # 1: 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
print(co.send(2))    # 3: 코루틴에 숫자 2를 보내고 코루틴에서 나온 값 출력
print(co.send(3))    # 6: 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력

# 바깥에서 send가 보낸 값은 x에 저장되고, 코루틴 바깥에 보낼 값은 total임


print('\n-------------\n')

# 보통 코루틴은 실행 유지를 위해 while True를 사용한 무한루프로 동작하는데 강제 종료를 원한다면 close 메서드를 사용함
def number_coroutine():
    while True:
        x = (yield)
        print(x, end=' ')
 
co = number_coroutine()
next(co)
 
for i in range(20):
    co.send(i)
 
co.close()    # 코루틴 종료(close 메서드 호출 시 코루틴이 종료될때 GeneratorExit 예외 발생)


