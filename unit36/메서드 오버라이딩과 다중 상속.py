# 프로그램에서 어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할 때 메서드 오버라이딩을 활용

class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):  # 기존 클래스의 greeting을 무시하고 만들어 사용함
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
 
james = Student()
james.greeting() # Student 의 greeting 메서드를 호출함


print('\n------\n')

# 다중 상속 (여러 기반 클래스로부터 상속을 받아 파생 클래스를 만드는 방법)


class Person:
    def greeting(self):
        print('안녕하세요.')
 
class University:
    def manage_credit(self):
        print('학점 관리')
 
class Undergraduate(Person, University):
    def study(self):
        print('공부하기')
 
james = Undergraduate()
james.greeting()         # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()    # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()            # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드


