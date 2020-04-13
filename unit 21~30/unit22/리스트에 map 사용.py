a = [1.1,2.2,3.3]
for  i in range(len(a)) :
    a[i] = int(a[i])

print(a) # [1, 2, 3]

# 위 아래 동일(아래는 map 사용)

a = list(map(int,a)
print(a)


# map 내에는 리스트 뿐 아니라 반복 가능한 객체면 모두 된다. (예 range 등)


         

         
