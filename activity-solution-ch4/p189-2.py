from roboid import *

hamster = Hamster()
hamster.tempo(120)
for i in range(2):
    hamster.note("C4", 1)
    hamster.note("E4", 1)
    hamster.note("G4", 1)
for i in range(3):
    hamster.note("A4", 1)
hamster.note("G4", 2)
hamster.note("OFF", 1)
for i in range(3):
    hamster.note("F4", 1)
for i in range(3):
    hamster.note("E4", 1)
for i in range(3):
    hamster.note("D4", 1)
hamster.note("C4", 2)
hamster.note("OFF", 1)
