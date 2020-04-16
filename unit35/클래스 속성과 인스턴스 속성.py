class Person:
    bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)  # ['책', '열쇠']
print(maria.bag)  # ['책', '열쇠']


# 클래스 속성은 클래스에 속해 있으며 모든 인스턴스에서 공유


print('\n-------------\n')


class Person:
    def __init__(self):
        self.bag = []  # 이와 같이 인스턴스 속성으로 만들면 인스턴트별로 독립되어있으며 서로 영향을 주지 않는다.
    
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)  # ['책']
print(maria.bag)  # ['열쇠']



print('\n-------------\n')


# 클래스 속성도 비공개 속성을 만들 수 있으며 __속성과 같이 밑줄 2개로 시작하면 비공개 속성이 됨



