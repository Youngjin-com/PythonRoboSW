from roboid import *

hamster = Hamster()
hamster.tempo(120)
for i in range(4):
    hamster.note("G4", 0.5)
hamster.note("E4", 1)
hamster.note("G4", 1)
for i in range(4):
    hamster.note("F4", 0.5)
hamster.note("D4", 1)
hamster.note("F4", 1)
