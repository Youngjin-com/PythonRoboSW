from roboid import *

hamster = Hamster()

number = 0

while True:
    # 손을 가져갈 때까지 반복한다.
    while hamster.left_proximity() < 40 and hamster.right_proximity() < 40:
        number = number % 3 + 1 # 1 ~ 3까지 계속 바뀐다.
        if number == 1:
            hamster.leds("RED")
        elif number == 2:
            hamster.leds("GREEN")
        else:
            hamster.leds("BLUE")

        wait(200) # 0.2초마다 값을 바꾼다.

    # 선택된 숫자를 화면에 표시한다.
    print('move', number, 'spaces')

    # 손을 치울 때까지 기다린다.
    while hamster.left_proximity() > 40 or hamster.right_proximity() > 40:
        wait(20)
