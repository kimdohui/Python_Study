a = []

for i in range(10) :
    a.append(0)

print(a)

# 리스트 생성(안에 0 10개로 채워짐)


print('---------  2\n')
a = []  # 빈 리스트

for i in range(3) :    # 안쪽 리스트로 사용 할 빈 리스트 생성
    line = []
    for j in range(2) :
        line.append(0)   # 안쪽 리스트에 0 추가
    a.append(line)     # 전체 리스트 안에 리스트 추가

print(a)  # [[0,0],[0,0],[0,0]]


print('\n---------  3\n')
a = [[0 for j in range(2)] for i in range(3)]
print(a)
# 결과는 위와 동일


print('\n---------  4\n')
a = [[0] *2 for i in range(3)]
print(a)
# 결과는 위와 동일



print('\n---------  5\n')
a = [1,2,3,4,5]
b = []

for i in a :
    line = []
    for j in range(i) :
        line.append(0)
    b.append(line)

print(b)  # [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]



    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]
 
print(sorted(students, key=lambda student: student[1]))  # 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students, key=lambda student: student[2]))  # 안쪽 리스트의 인덱스 2를 기준으로 정렬

# 2차원리스트 정렬은 sorted로
