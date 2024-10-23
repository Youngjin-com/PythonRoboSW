import turtle
from roboid import *

turtle.shape('turtle')

hamster = Hamster()
xlist = [] # 가로 방향에 대한 리스트
ylist = [] # 세로 방향에 대한 리스트
xsum = 0.0 # 가로 방향에 대한 합
ysum = 0.0 # 세로 방향에 대한 합

def calc_sum(sum, list, value, num):
    list.append(value) # 새로운 값 value를 list의 제일 뒤에 추가한다.
    sum += value # value를 sum에 더한다.
    if len(list) > num: # num 개수만큼 모았으면
        sum -= list.pop(0) # 가장 예전 값(list의 제일 앞, 즉 인덱스 0에 있는 값)을 저장소에서 제거하고 합에서 뺀다.

    return sum

while True:
    x = -round(hamster.acceleration_y() / 1500.0) * 30
    y = -round(hamster.acceleration_x() / 1500.0) * 30

    xsum = calc_sum(xsum, xlist, x, 10) # 가로 방향에 대한 합 (값의 최대 개수는 10개)
    ysum = calc_sum(ysum, ylist, y, 10) # 세로 방향에 대한 합 (값의 최대 개수는 10개)
    x = round(xsum / len(xlist)) # 가로 방향에 대한 평균
    y = round(ysum / len(ylist)) # 새로 방향에 대한 평균

    turtle.goto(x, y)

    wait(20) # 너무 빨리 반복하지 않도록 한다.
