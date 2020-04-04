print('and')
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# and 연산자는 둘 다 True일때만 True가 나옴

print(' ')
print('or')
print(True or True)      # True
print(True or False)     # True
print(False or True)     # True
print(False or False)    # False   

# or 연산자는 둘 중 하나라도 True일때 True가 나옴

print(' ')
print('not')
print(not True)
print(not False)

# not 연산자는 논릿값을 뒤집음( False -> True  , True -> False 가 됨 )


print(' ')
print(not True and False or not False)  #False

# and,or,not 연산자가 식 하나에 있으면 not,and,or 순으로 판단한다.


print(' ')
print(10 == 10 and 10 != 10)  # True and False -> False
print(not 1 is 1.0) # not False -> True
print(10>3 or 10<3) #True or False -> True

# 비교 연산자를 먼저 판단한 뒤 이 결과를 가지고 논리 연산자를 판단함


print(' ')
print(bool(1))        # True
print(bool(0))        # False
print(bool(1.2))      # True
print(bool('False'))  # True
print(bool(''))

# bool에서 정수 0을 제외한 나머지는 True , 0은 False 이다.
# bool은 문자열 내용 자체는 판단하지 않으며 값만 있으면 True가 나옴('', "" 과 같은 빈 문자열은 False)


print(' ')
print(True and 'python')   # python
print('python' and True)   # True
print(False and 'python')  # False

# (python은 불로 따지면 True가 되서 True가 될거 같지만 파이썬에서 논리 연산자는 마지막으로 단락 평가를 실시한 값을 그대로 반환)
# 똑같은 이유로 'python'은 True이므로 뒤에 값이 그대로 출력되어 True가 출력됨
# 만약 and 앞에 값이 False인 경우 첫번째 값만으로 결과가 결정나기 떄문에 첫번째 값인 False가 반환된다.(0을 앞에 넣으면 0으로 반환된다.)

print(' ')
print(True or 'python')   # True
print('python' or True)   # python
print(False or 'python')  # python

# or은 앞이 True라면 True기 때문에 첫번째 값만으로 결과가 측정되므로 첫번째 값이 출력된다.
# or은 앞이 False라면 뒤를 바야 알 수 있기 때문에 python을 반환한다.



