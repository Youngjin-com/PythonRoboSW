from roboid import *

hamster = Hamster()

while True:
    key = Keyboard.read() # 키보드 이벤트를 얻는다.
    if key: # 키보드 이벤트가 있으면
        if key == Keyboard.UP: # 위쪽 방향키
            hamster.wheels(50) # 앞으로 이동한다.
        elif key == Keyboard.DOWN: # 아래쪽 방향키
            hamster.wheels(-50) # 뒤로 이동한다.
        elif key == Keyboard.LEFT: # 왼쪽 방향키
            hamster.wheels(-50, 50) # 왼쪽으로 회전한다.
        elif key == Keyboard.RIGHT: # 오른쪽 방향키
            hamster.wheels(50, -50) # 오른쪽으로 회전한다.
        elif key == ' ': # 스페이스 키
            hamster.stop() # 정지한다.

    wait(20) # 너무 빨리 반복하지 않도록 한다.
