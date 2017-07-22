# Copyright (c) 2017 Nicolas P. Rougier and Fabien C. Y. Benureau
# Release under the BSD 2-clause license
# Tested with CPython 3.6.1 / macOS 10.12.4 / 64 bits architecture
import platform, datetime, json
import random

def provenance():
    """Retrieve data about the execution environment."""
    return {'python'   : {'implementation': platform.python_implementation(),
                          'version'       : platform.python_version_tuple(),
                          'compiler'      : platform.python_compiler(),
                          'branch'        : platform.python_branch(),
                          'revision'      : platform.python_revision()},
            'platform' : platform.platform(),
            'timestamp': datetime.datetime.utcnow().isoformat()+'Z'}  # Z stands for UTC

def walk(n, seed):
    """Return a `n` steps random walk.

    `seed` is used to initialized the Mersene Twister random number generator."""
    random.seed(seed)
    rndwalk, total = [], 0
    for i in range(10):
        step = +1 if random.uniform(-1,+1) > 0 else -1
        total += step
        rndwalk.append(total)
    return rndwalk

# Unit test
assert walk(10, 1) == [-1, 0, 1, 0, -1, -2, -1, 0, -1, -2]

def generate_results(n, seed, filename='results-R4'):
    """Generate results and save them to disk as a JSON file"""
    w = walk(n, seed)

    results = {'data': w, 'n': n, 'seed': seed, 'provenance': provenance()}
    with open(filename + '.json', 'w') as fd:
        json.dump(results, fd)
    return results

if __name__ == '__main__':
    print(generate_results(10, 1)['data'])
