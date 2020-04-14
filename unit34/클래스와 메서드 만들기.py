class Person:
     def greeting(self):
         print('hello')

# 클래스에 메서드 만들기(메서드는 클래스 내의 함수)
# 클래스 이름은 변수와 규칙이 동일하며 첫 매개변수는 반드시 self를 지정해야 함)


hana = Person()  # hana가 Person의 인스턴트 이다.

# 클래스 사용방법은 위와 같다. / 클래스에 괄호를 붙인 뒤 변수에 할당함

hana.greeting()

# 메서드 호출하기( 인스턴스 . 메서드() )



print('\n-----------\n')
class Person:
    pass

hana = Person()
print(isinstance(hana,Person))

# 특정 클래스의 인스턴트인지 확인하기 위해서는 isinstance함수를 사용함
