import turtle as t

t.shape('turtle')
for i in range(4) :
    t.forward(100)
    t.right(90)

# 사각형 그리기



t.shape('turtle')
for i in range(5) :
    t.forward(100)
    t.right(360/5)

# 오각형 그리기 ( 다각형 외각의 합은 360이니 오각형의 한 외각 크기는 360 / 5 이다.)



t.shape('turtle')
for i in range(6) :
    t.forward(100)
    t.right(360/6)


# 육각형 그리기


n = int(input())
t.shape('turtle')
t.color('red')
t.begin_fill()
for i in range(n) :
    t.forward(100)
    t.right(360/n)
t.end_fill()

# 원하는 다각형 만들기
# (+ t.color로 색을 지정한뒤 t.begin_fill()과 end()로 색칠구간 지정)
# color뒤에 red같은 명칭 말고 코드도 가능 #000000등


