a = [i for i in range(10)]
print(a)

# 0부터 9까지 숫자를 생성해 리스트 생성

print()
print('-------- 2')
print()

a = [i+2 for i in range(3)]  # [2,3,4]
print(a)
a = [i*3 for i in range(3)] # 0 3 6
print(a)
# i 뒤에 어떻게 써는지에 따라 출력 값이 달라진다.


print()
print('-------- 3')
print()

a = [i for i in range(10) if i%2==0] # if문을 사용하여 2의 배수만 추려냄
print(a)

# 리스트의 표현식에서 if문 사용



print()
print('-------- 4')
print()

 a = [i * j for j in range(2, 10) for i in range(1, 10)]
 print(a)

 # 리스트 내에 for문 여러번 쓰기
