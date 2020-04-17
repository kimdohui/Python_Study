class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):  # Person 클래스 상속
    def study(self):
        print('공부하기')
 
james = Student()
james.greeting()    # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.study()       # 공부하기: 파생 클래스 Student에 추가한 study 메서드


# 상속 받을 class를 괄호 안에 넣음 (이렇게 하면 Person 클래스 기능을 받은 student 클래스가 됨)

# 상속 관계를 확인하고 싶다면 issubclass함수를 사용하면 된다

print(issubclass(Student, Person)) # TRUE




print('\n-------------\n')


class Person:
    def greeting(self):
        print('안녕하세요.')
 
class PersonList:
    def __init__(self):
        self.person_list = []    # 리스트 속성에 Person 인스턴스를 넣어서 관리
 
    def append_person(self, person):    # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)


# 위와 같은 경우 Person 클래스와 PersonList 클래스가 상속 관계가 아닌 포함관계이다.
# 
