import bezier
import json
import seaborn
import numpy as np
import matplotlib.pyplot as plt

with open("patterns.json", "r") as jsonfile:
    info = json.load(jsonfile)
print(info["lines"])

seaborn.set()

for i in range(len(info["lines"])):
    if i == 0:
        node = np.asfortranarray(info["lines"][i])
        curve = bezier.Curve(node, degree=2)
        ax = curve.plot(num_pts=256)
    else:
        node = np.asfortranarray(info["lines"][i])
        curve = bezier.Curve(node, degree=2)
        _ = curve.plot(num_pts=256, ax=ax)

_ = ax.axis("scaled")
_ = ax.set_xlim(0, 80)
_ = ax.set_ylim(0, 80)
plt.show()