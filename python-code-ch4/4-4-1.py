from roboid import *

hamster = Hamster()

left = False
while True:
    key = Keyboard.read() # 키보드 이벤트를 얻는다.
    if key == ' ': # 스페이스 키를 눌렀으면
        left = not left # 방향을 반대로 한다.

        if left: # 왼쪽 방향이면
            hamster.wheels(0, 50)
        else: # 오른쪽 방향이면
            hamster.wheels(50, 0)

    wait(20) # 너무 빨리 반복하지 않도록 한다.
