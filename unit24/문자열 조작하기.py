s = 'Hello, world!'
s = s.replace('world!', 'Python')
print(s)

# 문자열 바꾸기

print('----------------')
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))

# 문자 바꾸기

print('----------------')
print('apple pear grape pineapple orange'.split())

# 문자열 분리하기


print('----------------')
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
# 문자열 연결


print('----------------')
print('apple'.upper())  # 대문자로
print('APPLE'.lower())  # 소문자로

print('----------------')
print('  apple  '.lstrip())  # 왼쪽 공백 삭제
print('  apple  ',rstrip())  # 오른쪽 공백 삭제
print('  apple  ',strip())  # 양쪽 공백 삭제


print('----------------')
print(' ,apple.'.lstrip(',.')  # 왼쪽 특정 문자 삭제
print(' ,apple.'.rstrip(',.')  # 오른쪽 특정 문자 삭제
print(' ,apple.'.strip(',.')  # 양쪽 특정 문자 삭제


print('----------------')
print(' ,apple.'.ljust(10)  # 지정된 길이로 문자열을 만든 뒤 왼쪽 정렬(남는 공간 공백)
print(' ,apple.'.rjust(10)  # 지정된 길이로 문자열을 만든 뒤 오른쪽 정렬(남는 공간 공백)
print(' ,apple.'.center(10)  # 지정된 길이로 문자열을 만든 뒤 양쪽 정렬(남는 공간 공백)

      # 남는 공백이 홀수라면 왼쪽에 공백이 하나 더 들어감



print('----------------')
print('python'.rjust(10).upper()) # 메서드 체이닝(메서드를 계속 연결할 수 있음)

print('----------------')
print('hi'.zfill(5))  # 지정된 길이만큼 문자열을 채우고 남는 공간은 0으로 채움

print('----------------')
print('apple pineapple'.find('pl'))  # 찾고 싶은 문자열 인덱스 위치 반환  // 2(젤 처음 해당 인덱스 반환)
print('apple pineapple'.lfind('pl'))  # 왼쪽부터 찾음
print('apple pineapple'.rfind('pl'))  # 오른쪽부터 찾음
# 단 없을 경우 -1 을 반환
      
print('----------------')
print( 'apple pineapple'.count('pl')) # 문자열 개수 세기  // 2 (먼저 해당하는 인덱스값 반환)

