i = 0
while True :
    print(i)
    i+= 1
    if i == 10 :
        break
    

# break 사용 시 반복문을 끝낼 수 있다. (for문도 사용 가능)

print('\n\n')
for i in range(100) :
    print(i)
    if i == 10 :
        break


print('\n\n')
for i in range(10) :
    if i%2==0:
        continue
    print(i)

# countinue를 사용하면 코드 실행을 건너뛸 수 없다. (while문도 사용가능)

print('\n')
i = 0
while i < 10 :
    i+= 1
    if i%2 == 0:
        continue
    print(i)

# countinue를 무한 루프에서 사용하면 끝나지 않고 계속 출력


print('\n')
count = int(input('반복 횟수 : '))
i = 0
while True :
    print(i)
    i += 1
    if i == count :
        break


start, stop = map(int, input().split())
 
i = start
 
while True:
    if(i>stop):
        break
    if(i%10 == 3):
        i+= 1
        continue
    print(i, end=' ')    
    i+= 1
