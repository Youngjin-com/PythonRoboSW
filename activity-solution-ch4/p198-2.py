from roboid import *

hamster = Hamster()
for i in range(2):
    hamster.move_forward(2)
    hamster.turn_left(1)
    hamster.move_forward(1)
    hamster.turn_left(1)
