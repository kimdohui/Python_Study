try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
    print(x)
except Exception as e:                             # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.', e)


# raise 에 예외를 저장하고 에러 메세지를 넣을 수 있다.



print('\n---------\n')


def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:                                 # x가 3의 배수가 아니면
            raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
        print(x)
    except Exception as e:                             # 함수 안에서 예외를 처리함
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise    # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김
 
try:
    three_multiple()
except Exception as e:                                 # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('스크립트 파일에서 예외가 발생했습니다.', e)


# 출력 결과

# 3의 배수를 입력하세요: 5 (입력)
# three_multiple 함수에서 예외가 발생했습니다. 3의 배수가 아닙니다.
# 스크립트 파일에서 예외가 발생했습니다. 3의 배수가 아닙니다.



# raise만 사용시 같은 예외를 상위 블록으로 넘기지만 raise에 다른 예외를 지정하고 에러메세지를 넣을 수 있음


raise RuntimeError('three_multiple 함수에서 예외가 발생했습니다.')



print('\n---------\n')

x = int(input('3의 배수를 입력하세요: '))
assert x % 3 == 0, '3의 배수가 아닙니다.'    # 3의 배수가 아니면 예외 발생, 3의 배수이면 그냥 넘어감
print(x)

# assert를 사용하여 예외를 발생시킬 수 있음(단 디버깅 모드에서만 실행)




print('\n---------\n')

# 예외 만드는 법


class NotThreeMultipleError(Exception):    # Exception을 상속받아서 새로운 예외를 만듦
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')
 
def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:                     # x가 3의 배수가 아니면
            raise NotThreeMultipleError    # NotThreeMultipleError 예외를 발생시킴
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)
 
three_multiple()
