a = [1,2,4]
print(len(a)) # 3

# len함수 활용 시 리스트 요소의 개수를 구할 수 있다.(튜플도 리스트와 결과 동일)

print(' ')
print(len(range(0,4,2)))
      
# range 또한 동일 (0,2) 총 2개

print(' ')
hi = 'hello world'
hello = '안녕'
print(len(hi))
print(len(hello))

# len을 문자열에 사용 시 문자 요소의 수를 알려준다.(이때 공백까지 포함되며 문자열을 묶은 따옴표는 제외함)
# 한글 문자열도 동일하다.

print(' ')
hello = '안녕'
print(len(hello.encode('utf-8')))

# UTF-8에서 한글 글자는 하나에 3바이트로 표현하므로 실제 차지 바이트 수는 6바이트이다.
                       
