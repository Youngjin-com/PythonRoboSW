from roboid import *

hamster = Hamster()
while True:
    print(hamster.left_proximity(), hamster.right_proximity())
    wait(20)
