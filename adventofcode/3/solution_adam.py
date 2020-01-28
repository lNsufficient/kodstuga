import numpy as np

with open('input') as f:
    wires = f.read()
wires = wires.split()
wires = [wire.split(',') for wire in wires]

max_dim = 50000

m = np.zeros((2, max_dim, max_dim), dtype=np.uint8)
for i, wire in enumerate(wires):
    x = max_dim // 2
    y = max_dim // 2
    for newpos in wire:
        dx = 0
        dy = 0
        direction = newpos[0]
        if direction == 'U':
            dy += 1
        elif direction == 'D':
            dy -= 1
        elif direction == 'R':
            dx += 1
        elif direction == 'L':
            dx -= 1

        change = int(newpos[1:])
        for _ in range(change):
            x += dx
            y += dy
            assert x >= 0 and y >= 0
            assert x < max_dim and y < max_dim
            m[i, y, x] = 1

m = np.sum(m, axis=0, dtype=np.uint8)
idx = np.nonzero(m == 2)
idx = np.stack(idx)
norms = np.linalg.norm(idx - max_dim // 2, axis=0, ord=1)
print(int(np.min(norms)))
