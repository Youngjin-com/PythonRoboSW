from roboid import *

hamster = Hamster()
hamster.tempo(120)
for i in range(2):
    for j in range(3):
        hamster.note("A4", 1)
        hamster.note("A4", 0.5)
    hamster.note("G4", 1.5)
