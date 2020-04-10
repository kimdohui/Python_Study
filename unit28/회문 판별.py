word = input('단어 입력: ')

is_palindrome = True  # 회문 판별 저장 변수
for i in range(len(word) // 2) :  # 문자열 길이 반만큼 반복
    if word[i] != word[-1-i] :  # 왼쪽 문자와 오른쪽 문자를 비교
        is_palindrome = False  # 왼쪽 문자와 오른쪽 문자가 다르면 회문이 아님
        break  # if문 탈출

print(is_palindrome)

# 회문 판별값 출력



print('\n----------------\n')
word = input('단어 입력: ')

print(word == word[::-1])  # word[::-1]은 문자열 전체에서 인덱스를 1씩 감소시키며 요소를 가져옴

# 즉 word[::-1]는 문자열을 뒤집는 것인데 회문은 거꾸로 읽어도 같으므로 두 개가 같으면 회문이다.
# 회문 판별값 출력



print('\n----------------\n')
word = 'level'
print(list(word) == list(reversed(word)))

# 리스트와 reverse사용하여 회문 판별


print('\n----------------\n')
word = 'level'
print(word == ''.join(reversed(word)))

# join은 구분자 문자열과 문자열 리스트의 요소를 연결하는데
# 여기서는 빈 문자열 ''에 reverse(word)요소를 연결하므로 반대로 된 문자열을 엉ㄷ을 수 있음


