a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b) # {1, 2, 3, 4, 5, 6}  / set.union(a, b)  과 결과가 같음

# | 연산자는 합집합을 구함


print(a & b) # {3,4}   /  set.intersection(a, b)과 결과가 같음

# & 연산자는 교집합을 구함



print(a - b)  #   {1,2}  / set.difference(a,b) 와 결과가 같음

# - 연산자는 차집합과 같음


print(a ^ b)  # {1,2,5,6}  /  set.symmetric_difference(a, b) 과 결과가 같음

# ^ 연산자는 대칭차집합과 같음(공통된 부분만 제회)



print('------------ ')


a = {1, 2, 3, 4}
a |= {5}  # a.update({5}) 와 같음
print(a)

# {1, 2, 3, 4, 5}


a = {1, 2, 3, 4}
a &= {1,2,3,4,5}  # a.intersection_update({1,2,3,4,5}) 와 같음
print(a)

# {1, 2, 3, 4}




a = {1, 2, 3, 4}
a -= {2}  #a.difference_update({2}) 와 같음
print(a)

# {1, 3, 4}



a = {1, 2, 3, 4}
a ^= {1,2} # a.symmetric_difference_update({1,2}) 와 같음
print(a)

# {3, 4}


print('------------ ')
a = {1, 2, 3, 4}
print(a == {1, 2, 3, 4})

# 세트가 같은지는 ==를 사용해 알 수 있음(같으면 True)

a.isdisjoint({5, 6, 7, 8})
# 세트가 겹치는지 확인(겹치는 요소가 없다면 True반환)
