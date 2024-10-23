from roboid import *

hamster = Hamster()
hamster.tempo(120)
for i in range(2):
    hamster.note("C4", 1.5)
    hamster.note("D4", 0.5)
    hamster.note("E4", 1)
    hamster.note("G4", 1)
    for j in range(3):
        hamster.note("D4", 0.5)
    hamster.note("E4", 0.5)
    hamster.note("C4", 1)
    hamster.note("OFF", 1)
