a = [10,20,30,40,50,60,70,80]
for i in a :
    print(i)

# 반복문으로 전체 출력


print()
print('-------- 3')
print()

a = [10,20,30]
for index,value in enumerate(a) :  # enumerate(a,start=1) 지정 시 인덱스가 1부터
    print(index,value)


# enumerate 사용 시 인덱스와 요소를 꺼낼 수 있다


print()
print('-------- 4')
print()

a = [10,20,30]
for i in range(len(a)) :    # for
    print(a[i])

print()
i=0 
while i < len(a) :          # while문
    print(a[i])
    i+=1
