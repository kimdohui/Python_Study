hello = 'hello world'
print(hello)

# hello world 를 작은 따옴표로 묶어서 문자열로 만들었음

print(' ')
hello = "Hello world"
print(hello)
hello = '''Hello world'''
print(hello)
hello = """Hello world"""
print(hello)
# 작은 따옴표 대신 큰 따옴표, 작은 따옴표 3개 , 큰 따옴표 3개를 사용해도 됨


print(' ')
hello = '''Hello world
안녕하세요
python이에요.'''
print(hello)

# 여러 줄로 된 문자열을 출력하고 싶다면 ''', """로 묶어준 뒤 안에 내용을 입력하면 됨


print(' ')
print(" 'Hello' ")
print(' "Hello" ')
print(''' hi
'misa' ''')

# 만약 문자열에 작은 따옴표(')를 사용하고 싶다면 큰 따옴표로 감싸주고, 큰 따옴표(")를 사용하고 싶다면 작은 따옴표로 감싸주면 된다.
# 이때 작은 따옴표(큰 따옴표) 안에 작은 따옴표(큰 따옴표)를 쓰면 오류가 발생한다.
# 단 여러 줄로 된 문자열 안에는 작은 따옴표, 큰 따옴표를 전부 넣을 수 있다.


print(' ')
print(' \'hello\' ')
print(" \"hello\" ")

# 만약 문자열에 ' 나 " 를 넣고 싶다면 \와 함께 쓰면 됨


print(' ')
print('hello\nmisa')

# 개행문자(\n)를 사용하면 따옴표 3개로 묶지 않고 여러 줄로 된 문자열을 사용할 수 있다.

