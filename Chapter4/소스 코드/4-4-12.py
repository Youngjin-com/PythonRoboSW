import random
from roboid import *

hamster = Hamster()

number = 0
position = 0 # 현재 위치
started = False # 출발한 이후인가?
corners = (0, 4, 7, 11) # 모퉁이 위치
score = 0 # 현재 점수
points = (0, 1, -1, 2, -2, 3, -3, 2, -2, 1, -1, 2, -2, 3) # 위치에 따른 점수

# 한 칸 이동한다.
# 위치가 모퉁이인 경우 왼쪽으로 회전한 후 앞으로 한 칸 이동
# 아니면 그냥 앞으로 한 칸 이동
def move():
    global started
    global position

    if started: # 처음 출발할 때는 왼쪽으로 회전하지 않게 한다.
        if position in corners: # 모퉁이에 있으면 왼쪽으로 회전
            hamster.board_left()
    else:
        started = True # 출발하였다.

    hamster.board_forward()
    position += 1
    if position > 13:
        position = 0

while True:
    # 손을 가져갈 때까지 반복한다.
    while hamster.left_proximity() < 40 and hamster.right_proximity() < 40:
        number = number % 3 + 1 # 1 ~ 3까지 계속 바뀐다.
        if number == 1:
            hamster.leds(Hamster.LED_RED)
        elif number == 2:
            hamster.leds(Hamster.LED_GREEN)
        else:
            hamster.leds(Hamster.LED_BLUE)

        wait(200) # 0.2초마다 값을 바꾼다.

    # 선택된 숫자를 화면에 표시한다.
    print('move', number, 'spaces')

    # 손을 치울 때까지 기다린다.
    while hamster.left_proximity() > 40 or hamster.right_proximity() > 40:
        wait(20)

    # 선택된 숫자만큼 이동한다.
    for i in range(number):
        move()
        print('position:', position) # 현재 위치 표시

    # 점수를 계산한다.
    if position == 0: # 출발 위치에 있으면
        score += random.randint(1, 3) # 1 ~ 3까지의 무작위 점수를 더한다.
    else:
        score += points[position] # 이동한 위치의 점수를 더한다.

    print('score:', score, '\n') # 현재 점수 표시