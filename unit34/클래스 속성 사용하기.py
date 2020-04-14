class Person:
    def __init__(self):  # __nit__ 메서드는 클래스에 괄호를 붙여 인스턴스를 만들때 호출되는 특별한 메서드이다.(객체 초기화)
        self.hello = '안녕하세요.'
 
    def greeting(self):
        print(self.hello)
 
james = Person()
james.greeting()    # 안녕하세요.



# self 는 인스턴스 자기 자신을 의미함 즉 여기서 __init__의 매개변수 self에 들어가는 값은 person()이라 할 수 있음
# self가 완성된 뒤 인스턴스에 할당되고 이후 메서드 호출 시 현재 인스턴스가 자동으로 매개변수 self에 들어옴


print('\n-----------\n')

class Person :
    def __init__(self,name,age):
        self.hello= 'hello'
        self.name = name
        self.age = age

    def greeting(self) :
        print('{0} 저는 {2}살 {1}입니다.'.format(self.hello,self.name,self.age))

hana = Person('하나',10)
hana.greeting()

print('\n')
print('이름 : ', hana.name)
print('나이 : ', hana.age)



# 클래스로 인스턴스를 만든 뒤에도 속성을 추가할 수 있지만 해당 인스턴스에만 생성됨


print('\n-----------\n')

class Person:
    __slots__ = ['name', 'age']    # name, age만 허용(다른 속성은 생성 제한)


# __slots__ 사용 시 특정 속성만 허용할 수 있음



print('\n-----------\n')

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦


    def pay(self, amount):
        self.__wallet -= amount   # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))

 
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
# maria.__wallet -= 10000    # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함

maria.pay(3000)



# 위와 같이 비공개 속성을 만들기 위해선 __ 를 앞에 붙여야 함(양쪽에 있을경우 비공개 속성이 아님)
# 비공개 속성을 변경하기 위해서는 메서드를 따로 작성해야 함


# 메서드도 클래스 바깥으로 드러내고 싶지 않을 때 __를 붙여 비공개 메서드를 만드는 것이 가능함








