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

