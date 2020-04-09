file = open('hello.txt','w') # w는 쓰기모드
file.write('hello')
file.close()

# 파일을 사용하기 위해서는 제일 먼저 open 함수로 파일을 열어서 객체를 얻어야 함
# 파일 객체를 얻은 뒤 write로 파일에 문자열을 씀
# 파일 쓰기가 끝났으면 close로 파일 객체를 닫음



file = open('hello.txt', 'r') # r은 읽기 모드
s = file.read()
print(s)
file.close()

# 파일의 내용을 읽을 수 있음


with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)

# with as 사용 시 자동으로 파일 객체를 닫음

print('\n---------------- \n')
with open('hello.txt' , 'w') as file :
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))
        

# 다음과 같이 저장
# Hello, world! 0
# Hello, world! 1
# Hello, world! 2


print('\n---------------- \n')
line = ['안녕\n','잘 부탁해']

with open('hello.txt', 'w') as file :
    file.writelines(line) # writelines는 리스트에 들은 문자열을 파일에 씀

# 리스트 내에 문자열 파일에 쓰기
# writelines 사용 시 반드시 리스트의 각 문자열에 개행문자를 붙여야 함
#  (안 그러면 한줄로 붙어서 리스트 형태로 가져옴)




with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    lines = file.readlines()
    print(lines)

# 파일의 내용을 한 줄씩 리스트로 가져옴



print('\n---------------- \n')

with open('hello.txt', 'r') as file: # hello.txt 파일을 읽기 모드(r)로 열기
    line = None   # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline() # 특성 상 읽을 줄이 없을 경우 빈 문자열 반환
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력


# 파일의 내용을 한 줄씩 읽음
#readline을 사용 시에는 while문을 사용해야 함(파일에 문자열이 몇줄인지 모르므로)




print('\n---------------- \n')
with open('hello.txt', 'r') as file:
    for line in file:    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

# for문을 이용해 파일의 내용을 한줄씩 읽음
