from roboid import *

hamster = Hamster()
hamster.tempo(120)
for j in range(3):
    hamster.note("F4", 0.5)
hamster.note("E4", 0.5)
hamster.note("D4", 0.5)
hamster.note("E4", 0.5)
hamster.note("F4", 1)
for j in range(3):
    hamster.note("F4", 0.5)
hamster.note("E4", 0.5)
hamster.note("D4", 0.5)
hamster.note("E4", 0.5)
hamster.note("F4", 1)
