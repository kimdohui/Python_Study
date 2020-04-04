for i in range(5) :
    for j in range(5) :
        print('*',end='')
    print() 
    
# 기본적인 별찍기

#   *****
#   *****
#   *****
#   *****
#   *****


print('\n')
for i in range(3) :
    for j in range(7) :
        print('*',end='')
    print()

#   *******
#   *******
#   *******


print('\n')
for i in range(5) :
    for j in range(5) :
        if(j <= i) :
            print('*',end='')
    print()

# 계단식 별찍기

#  *
#  **
#  ***
#  ****
#  *****


print('\n')
for i in range(5) :
    for j in range(5) :
        if (i==j) :
            print('*',end='')
        else :
            print(' ',end='')
    print()


# 대각선 별 찍기
#  *
#   *
#    *
#     *
#      *


num = int(input())
for i in range(num) :    
     for z in range(num) :
        if (num)<=(i+z) :
            print('*', end='')
        else :
            print(' ',end='')
     for z in range(num+1) :
        if(z <= i) :
            print('*', end='')
     print('')


# 삼각형 출력 (위 아래)


height = int(input())
for i in range(height):
    for j in reversed(range(height)):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(height):
        if j < i:
            print('*', end='')
    print()
