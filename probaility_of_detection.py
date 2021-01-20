import random
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

NUM_EQUIV_VOLUMES = 1000
MAX_CIVS = 5000
TRIALS = 1000
CIV_STEP_SIZE = 100

x = []
y = []

for num_civs in range(2,MAX_CIVS + 2,CIV_STEP_SIZE):
    #print(num_civs)
    civs_per_vol = num_civs/NUM_EQUIV_VOLUMES
    #print(civs_per_vol)
    num_single_civs = 0

    for trial in range(TRIALS):
        locations = []
        while len(locations)<num_civs:
            location = random.randint(1,NUM_EQUIV_VOLUMES)
            locations.append(location)
    print(len(locations))

