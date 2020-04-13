name = 'maria'
print('I am %s.' % name)

# 서식 지정자로 문자열 넣기 (%s를 문자열 내에 넣고 %를 쓴 뒤 값을 넣어주면 값이 %s 자리에 대신 출력)
# 숫자도 지정 됨 ( 숫자 %d    실수 %f )


print('-------------------')
print('%10s' % 'python')
# 문자열 길이를 10으로 만든 뒤 지정된 문자열을 넣고 오른쪽으로 정렬함
# 문자열 정렬은 자릿수가 다른 숫자를 출력할 때 유용


print('-------------------')
print('%-10s' % 'python')
# 왼쪽 정렬은 -를 붙여주면 됨


print('-------------------')
print('Today is %d %s.' % (3, 'April'))
# 문자열 안에 값을 여러 개 넣을 수 있음



print('-------------------')
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)) #'Hello, Python 3.6 Script'
# {} 안에 인덱스를 넣은 뒤 format으로 값을 넣을 수 있다.
# 같은 인덱스를 여러 번 쓸 수 있음
# 인덱스 생략 시 format에 지정한 값이 순서대로 들어감

print('-------------------')
print('Hello, {language} {version}'.format(language='Python', version=3.6))
# {}에 인덱스 대신 이름을 지정할 수도 있음


print('-------------------')
language = 'Python'
version = 3.6
f'Hello, {language} {version}'


# 문자열 포매팅에 변수를 그대로 사용할 수 있음(문자열 앞에 f붙일 것)
