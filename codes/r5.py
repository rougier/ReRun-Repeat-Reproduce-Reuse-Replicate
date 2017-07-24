# Copyright (c) 2017 Nicolas P. Rougier and Fabien C.Y. Benureau
# Release under the BSD 2-clause license
# Tested with Python 3.6.1 / Numpy 1.12.0 / macOS 10.12.4 / 64 bits architecture
import random
import numpy as np

def walk(rng, n):
    """Random walk for n steps."""
    # Note: We consider 0 to be a positive step
    steps = 2*(rng.uniform(-1,+1,n) > 0) - 1
    return steps.cumsum().tolist()

def rng(seed):
    """Return a random number generator initialized with seed."""
    rng = random.Random()
    rng.seed(seed)
    _, keys, _ = rng.getstate()
    rng = np.random.RandomState()
    state = rng.get_state()
    rng.set_state((state[0], keys[:-1], state[2], state[3], state[4]))
    return rng

if __name__ == '__main__':
    # Unit test
    assert walk(rng(seed=1), 10) == [-1, 0, 1, 0, -1, -2, -1, 0, -1, -2]

    # Random walk for 10 steps
    seed = 1
    x = walk(rng(seed=seed), 10)

    # Display & save results
    print(x)
    with open("results-R5-%d.txt" % seed, "w") as file:
        file.write(str(x))
