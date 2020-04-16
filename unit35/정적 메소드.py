class Calc:
    @staticmethod  # 정적 메서드는 매개 변수에 self를 지정하지 않음(인스턴스 속성에는 접근 불가)
    def add(a, b):
        print(a + b)
 
    @staticmethod
    def mul(a, b):
        print(a * b)
 
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출

# 정적 메소드는 인스턴스를 통하지 않고 클래스에서 바로 호출할 수 있다.
# 정적 메소드는 실행이 외부 상태에 영향을 끼치지 않는 순수 함수를 만들 때 사용함


print('\n-------------\n')


class Person:
    count = 0    # 클래스 속성
 
    def __init__(self):
        Person.count += 1    # 인스턴스가 만들어질 때
                             # 클래스 속성 count에 1을 더함
 
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근
 
james = Person()
maria = Person()
 
Person.print_count()    # 2명 생성되었습니다.


# 클래스 메서드는 정적 메서드처럼 인스턴스 없이 호출할 수 있다는 점은 같지만
# 클래스 메서드는 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용함
