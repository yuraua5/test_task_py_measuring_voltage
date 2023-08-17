import numpy as np
import statistics

data = [364, 373, 358, 394, 378, 379, 357, 364, 350, 363, 392, 368, 359, 375, 399, 365, 379, 357, 380]

mean = np.mean(data)

median = np.median(data)

modes = statistics.multimode(data)

std_dev = np.std(data)

print("Mean:", mean)
print("Median:", median)
print("Mode:", modes)
print("Standard Deviation:", std_dev)
