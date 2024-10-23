from roboid import *

hamster = Hamster()

# 딕셔너리를 만든다.
notes = {
    " ": "OFF", # 소리를 끈다.
    "a": "C4", # 도
    "s": "D4", # 레
    "d": "E4", # 미
    "f": "F4", # 파
    "g": "G4", # 솔
    "h": "A4", # 라
    "j": "B4", # 시
    "k": "C5", # 도
    "l": "D5", # 레
    ";": "E5", # 미
    "'": "F5" # 파
}

while True:
    key = Keyboard.read() # 키보드 이벤트를 얻는다.
    if key and key in notes: # 키보드 이벤트가 딕셔너리에 있으면
        hamster.note("OFF", 0.05) # 0.05 박자로 잠시 쉰다.
        hamster.note(notes[key]) # 키보드의 키에 해당하는 음을 소리낸다.

    wait(20) # 너무 빨리 반복하지 않도록 한다.
