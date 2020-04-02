x = 10
if x == 10 :
    print(x)

# if문 사용하기

print(' ')
y = 20
if y == 20 :
    pass
# pass 사용 시 코드를 생략하고 넘어갈 수 있다.(원래 if문에 아무 코드도 넣지 않으면 에러 발생)
# if 다음에 오는 코드들은 반드시 들여쓰기 깊이가 같아야 한다.


print(' ')
x = 10

if x >= 5 :
     print('5 이상')

     if x >= 7 :
         print('7 이상')

     if x == 11 :
         print(' x = 11 이다')


# 이렇게 if문을 중첩하여 사용할 수 있다.( if문에 소속된 구문은 들여쓰기를 꼭 해줄 것 )


print(' ')
x = int(input())

if x == 10 :
    print('10이다')

if x == 20 :
    print('20이다')
    
