from roboid import *

hamster = Hamster()

hamster.wheels(30, 30) # 앞으로 이동한다.

count = 0
white = False
while True:
    if hamster.left_floor() > 70 and hamster.right_floor() > 70:
        white = True # 하얀색 종이 위에 있다.
    elif white and (hamster.left_floor() < 20 or hamster.right_floor() < 20): # 하얀색에서 검은색으로 바뀌면
        white = False

        # 개수를 하나 증가시키고 화면에 출력한다.
        count += 1
        print('count:', count)

    wait(20) # 너무 빨리 반복하지 않도록 한다.
