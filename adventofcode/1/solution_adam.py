import numpy as np

with open('input') as f:
    masses = f.read()
masses = masses.split()
masses = [float(mass) for mass in masses]
fuel = [int(mass / 3) - 2 for mass in masses]
print(np.sum(fuel))
