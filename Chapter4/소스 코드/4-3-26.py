from roboid import *

hamster = Hamster()

hamster.wheels(30, 30) # 앞으로 이동한다.

tick = 0
code = ''
while True:
    if hamster.left_floor() > 80 and hamster.right_floor() > 80: # 하얀색 종이 위에 있으면
        if tick > 0:
            if tick > 40: # 선이 굵다.
                code += '-'
            else: # 선이 가늘다.
                code += '.'

            # 바코드 확인
            print(code)
            if code == '.--.':
                print('peanut')
                code = ''
            elif code == '-..-':
                print('cheese')
                code = ''
        tick = 0
    elif hamster.left_floor() < 20 or hamster.right_floor() < 20: # 검은색 선 위에 있으면
        tick += 1

    wait(20) # 너무 빨리 반복하지 않도록 한다.
