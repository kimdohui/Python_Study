import turtle as t

t.shape('turtle')
t.circle(120)

# 반지름이 120인 원 그리


n = 50  # 반복 횟수
t.shape('turtle')
t.speed('fastest')  # 속도를 가장 빠르게 설정
for i in range(n) :
    t.circle(120)
    t.right(360/n)

# 360/30을 계산하면 12인데 오른쪽으로 12도씩 회전하면서 원을 겹친다.


t.shape('arrow')  # 이외에도 turtle,circle,square,triangle,classic 등도 있음
t.speed('fastest')
for i in range(450) :
    t.forward(i)    # 반복할때마다 선이 길어
    t.right(93)  # 미세하게 틀어진 사각형


