from roboid import *

hamster = Hamster()
hamster.tempo(120)
for i in range(6):
    hamster.note("G4", 0.5)
hamster.note("E4", 1)
for i in range(6):
    hamster.note("A4", 0.5)
hamster.note("G4", 1)
