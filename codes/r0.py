import random

x = 0
for i in xrange(10):
    step = random.choice([-1,+1])
    x += step
    print x,
