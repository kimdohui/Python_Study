    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'
 
james = Student()
print(james.school)
print(james.hello)    # 기반 클래스의 속성을 출력하려고 하면 에러가 발생함

# 즉 Person의 __init__ 메서드가 호출되지 않으면 self.hello 도 실행되지 않아서 속성이 만들어지지 않음
# (기반 클래스를 초기화하지 않음) 이럴땐 super()를 사용해주면 됨


print('\n---------\n')

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()                # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장'
 
james = Student()
print(james.school)
print(james.hello)


# Person의 __init__ 메서드를 호출해주면 기반 클래스가 초기화되어서 속성이 만들어짐


# 파생 클래스에 __init__ 메서드가 없다면 기반 클래스의 __init__이 자동으로 호출되므로 기반 클래스의 속성을 사용할 수 있음.
