
import matplotlib.pyplot as plt
import numpy as np


def draw_branch(depth, x=0, y=0, angle=np.pi / 2, length=10):
    if depth == 0:
        return

    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    plt.plot([x, x_end], [y, y_end], lw=depth * 0.5)

    new_length = length * 0.8
    angle_offset = np.pi / 4

    draw_branch(depth - 1, x_end, y_end, angle + angle_offset, new_length)

    draw_branch(depth - 1, x_end, y_end, angle - angle_offset, new_length)


try:
    depth = int(input("Enter the recursion depth (reccomended from 1 to 12):"))
except ValueError:
    print("invalid value. Default depth will be used (8)")
    depth = 8


plt.figure(num=f"Pythagoras Tree Fractal (Depth: {depth})", figsize=(8, 8))
plt.axis('off')

draw_branch(depth)

plt.show()
