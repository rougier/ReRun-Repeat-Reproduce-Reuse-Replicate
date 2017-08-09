# Tested with Python 3
import random

random.seed(0) # RNG initialization

walk, total = [], 0
for i in range(10):
    step = random.choice([-1,+1])
    total += step
    walk.append(total)

print(walk)
with open("results-R2.txt", "w") as file: # Saving output to disk
    file.write(str(walk))
