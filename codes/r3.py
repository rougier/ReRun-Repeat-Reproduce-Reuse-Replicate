# Copyright (c) 2017 Nicolas P. Rougier and Fabien C. Y. Benureau
# Release under the BSD 2-clause license
# Tested with CPython 3.6.1 / macOS 10.12.4 / 64 bits architecture
import platform, datetime
import random
import git

def git_info(): # Retrieve the code version
    repo = git.Repo(os.path.dirname(__file__), search_parent_directories=True)
    return {'hash': repo.head.object.hexsha,
            'dirty': repo.is_dirty()}

def provenance(): # Get info about the execution environment
    return {'python'   : {'implementation': platform.python_implementation(),
                          'version'       : platform.python_version_tuple(),
                          'compiler'      : platform.python_compiler(),
                          'branch'        : platform.python_branch(),
                          'revision'      : platform.python_revision()},
            'platform' : platform.platform(),
            'git_info' : git_info(),
            'timestamp': datetime.datetime.utcnow().isoformat()+'Z'}  # Z stands for UTC

def walk():
    promenade, total = [], 0
    for i in range(10):
        step = +1 if random.uniform(-1,+1) > 0 else -1
        total += step
        promenade.append(total)
    return promenade

# Unit test
random.seed(1)
assert walk() == [-1, 0, 1, 0, -1, -2, -1, 0, -1, -2]

# Random walk for 10 steps
seed = 1
random.seed(seed)
w = walk()

# Display & save results
print(w)
results = {'data': w, 'seed': seed, 'provenance': provenance()}
with open("results-R3.txt", "w") as fd:
    fd.write(str(results))
