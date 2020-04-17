from abc import * # 추상 클래스를 만드려면 import로 abc모듈을 가져와야 함

from abc import *
 
class StudentBase(metaclass=ABCMeta):
    @abstractmethod # import abc로 모듈을 가져올 시 사용해야 함
    def study(self):
        pass

 
class Student(StudentBase):
    def study(self):  # 추상 클래스에 사용한 베이스를 사용함
        print('공부하기')
 
james = Student()
james.study()

# 추상 클래스에서 상속받은 메서드를 구현하지 않을 경우 에러 발생

# 추상 클래스는 인스턴스로 만들 수 없기 때문에 pass를 넣어준다.
