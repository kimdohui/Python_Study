for i in range(100) :
    if i%3 == 0 and i%5 == 0 :
        print('FizzBuzz')
    elif i%3== 0 :
        print('Fizz')
    elif i%5 == 0 :
        print('Buzz')
    else :
        print(i)


# 1~100 을 출력하는데 3의 배수는 Fizz  5의 배수는 Buzz 로 출력하기(공배수는 FizzBuzz) 
# 아래는 논리 연산자를 사용하지 않은 FizzBuzz

print('\n')
for i in range(100) :
    if i%15 == 0 :
        print('FizzBuzz')
    elif i%3== 0 :
        print('Fizz')
    elif i%5 == 0 :
        print('Buzz')
    else :
        print(i)


# 아래는 코드를 단축한 Fizz Buzz

for i in range(1,101) :
    print('Fizz'*(i%3 == 0) + 'Buzz' *(i%5==0) or i)

# *를 사용하여 만약 뒤에 식이 True라면 fizz나 buzz를 출력하게 만들었다
# fizz나 buzz 과 i 중 하나만 출력함(앞이 참이면 뒤 i 는 무시)
    
