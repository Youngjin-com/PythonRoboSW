from roboid import *

hamster = Hamster()

number = 0
position = 0 # 현재 위치
score = 0 # 현재 점수
points = (0, 1, -1, 2, -2, 3, -3, 2, -2, 1) # 위치에 따른 점수

# 한 칸 이동한다.
def move():
    global position

    hamster.board_forward()
    position += 1
    if position > 9:
        position = 0

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

    # 선택된 숫자만큼 이동한다.
    for i in range(number):
        move()
        print('position:', position) # 현재 위치 표시

    # 점수를 계산한다.
    score += points[position] # 이동한 위치의 점수를 더한다.

    print('score:', score, '\n') # 현재 점수 표시
