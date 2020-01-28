import numpy as np
import math

with open('input') as f:
    masses = f.read()
masses = masses.split()
masses = [float(mass) for mass in masses]

mass_to_fuel = lambda mass: math.trunc(mass / 3) - 2

fuel = [mass_to_fuel(mass) for mass in masses]
fuel_sum = np.sum(fuel)
print('Solution 1a:', fuel_sum)

for fuel_ in fuel:
    while True:
        fuel_for_fuel = mass_to_fuel(fuel_)
        if fuel_for_fuel <= 0:
            break
        fuel_sum += fuel_for_fuel
        fuel_ = fuel_for_fuel
print('Solution 1b:', fuel_sum)
