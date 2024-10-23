from roboid import *

hamster = Hamster()

hamster.wheels(30, 30) # 앞으로 이동한다.

count = 0
while True:
    if hamster.left_floor() < 20 or hamster.right_floor() < 20: # 검은색 선 위에 있으면
        # 개수를 하나 증가시키고 화면에 출력한다.
        count += 1
        print('count:', count)

        hamster.wheels(30, 30) # 1초 동안 앞으로 이동한다.
        wait(1000)

    wait(20) # 너무 빨리 반복하지 않도록 한다.
