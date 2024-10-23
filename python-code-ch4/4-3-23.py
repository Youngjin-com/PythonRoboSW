from roboid import *

hamster = Hamster()

while hamster.left_floor() > 20 and hamster.right_floor() > 20: # 정지선을 만날 때까지
    hamster.wheels(30) # 앞으로 이동한다.
    wait(20) # 너무 빨리 반복하지 않도록 한다.

hamster.stop() # 정지한다.
