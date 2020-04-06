a = [[10,20],[30,40],[50,60]]
for x,y in a:   # in 앞에 변수 개수는 2차원 리스트에서 가로와 일치해야 함
    print(x,y)

# 리스트 안쪽 요소 출력



print('---------  2\n')
a = [[10,20],[30,40],[50,60]]

for i in a:  # 가로 한줄씩 꺼냄
    for j in i:  # 가로 한줄에서 요소 하나씩 꺼냄
        print(j, end=' ')
    print()


print('---------  3\n')
a = [[10,20],[30,40],[50,60]]

for i in range(len(a)) :  # 세로 크기
    for j in range(len(a[i])):  # 가로 크기
        print(a[i][j], end=' ')
    print()



print('---------  4\n')
a = [[10,20],[30,40],[50,60]]

i = 0
while i < len(a) :  #세로 한줄
    x,y = a[i]
    print(x,y)
    i+=1


print('---------  5\n')
a = [[10,20],[30,40],[50,60]]

i = 0
while i < len(a) :  # 세로 크기
    j = 0
    while j < len(a[i]) :  # 가로 크기
        print(a[i][j], end=' ')
        j += 1
    print()
    i+=1
    
