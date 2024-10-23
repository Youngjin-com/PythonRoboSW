from roboid import *

hamster = Hamster()

while True:
    key = Keyboard.read() # 키보드 이벤트를 얻는다.
    if key: # 키보드 이벤트가 있으면
        if key == 'a':
            hamster.note("C4") # 도
        elif key == 's':
            hamster.note("D4") # 레
        elif key == 'd':
            hamster.note("E4") # 미
        elif key == 'f':
            hamster.note("F4") # 파
        elif key == 'g':
            hamster.note("G4") # 솔
        elif key == 'h':
            hamster.note("A4") # 라
        elif key == 'j':
            hamster.note("B4") # 시
        elif key == 'k':
            hamster.note("C5") # 도
        elif key == 'l':
            hamster.note("D5") # 레
        elif key == ';':
            hamster.note("E5") # 미
        elif key == "'":
            hamster.note("F5") # 파
        elif key == ' ': # 스페이스 키
            hamster.note("OFF") # 소리를 끈다.

    wait(20) # 너무 빨리 반복하지 않도록 한다.
