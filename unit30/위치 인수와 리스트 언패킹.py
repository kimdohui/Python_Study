print(1,2,3)

# 이와 같이 함수에 인수를 순서대로 넣는 방식을 위치 인수라 함

print('\n--------------- \n')
def print_num(a,b,c):
    print(a)
    print(b)
    print(c)
    
print_num(10,20,40)


print('\n--------------- \n')

x = [10,20,30]
print_num(*x)

# 언패킹 사용(인수를 순서대로 넣기 위해 리스트나 튜플을 사용할 수 있음 )
# 인수의 개수가 정해지지 않은 가변인수로 사용가능

print('\n--------------- \n')

def person_info(name,age):
    print('이름: ', name)
    print('나이: ',age)

person_info('하하',11)

# 위의 함수를 이용하기 위해서는 인수의 순서에 맞게 집어넣어야 한다.
# 파이썬은 인수의 순서와 용도를 매번 기억하지 않도록 키워드 인수라는 기능을 제공함

person_info(name='gkgk',age=10)

# 키워드 인수 사용시 인수의 순서를 맞추지 않아도 
