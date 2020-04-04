print()
print('-------- 1')
print()

a = [10,20,30]
smallest  = a[0]
for i in a:
    if i < smallest:
        smallest =  i
print(smallest)
        
# 작은 값 구하기

print()
print('-------- 2')
print()

a = [10,20,30]
largest = a[0]
for i in a:
    if i > largest :
        largest = i
print(largest)

# 큰 값 구하기


print()
print('-------- 3')
print()

a = [10,20,30]
a.sort()
print(a[0])
a.sort(reverse=True)
print(a[0])

# 오름차순 내림차순 한 뒤 값 출력해서 최솟 , 최댓 값 찾기


print()
print('-------- 4')
print()

a = [10,20,30]
print(min(a))
print(max(a))

# 파이썬 내장 함수 min , max 사용 시 최댓값 최솟값을 쉽게 구할 수 있다.


print()
print('-------- 5')
print()

a = [10,20,30]
x = 0
for i in a:
    x+= i
print(x)

# 리스트 요소 합 구하기


print()
print('-------- 6')
print()

a = [10,20,30]
print(sum(a))
