def plus_ten(x) :
    return x + 10

print(plus_ten(10))

# 입력받은 숫자에 10만큼 더하는 함수

plus_ten = lambda x : x+10

print(plus_ten(10))

# 위의 함수를 람다 표현식으로 사용하기


print('\n-----------\n')
print((lambda x:x+10)(3))

# 람다 표현식 자체를 호출하기(변수에 할당하는 과정없이 호출 가능)

# 람다 표현식 안에는 새 변수를 만들 수 없음(단 람다 표현식 바깥에 있는 변수는 사용 가능)



print('\n-----------\n')
print(list(map(lambda x: +10, [1,2,3])))

# 위와 같이 람다 표현식을 매개변수로 넣을 수 있다.


