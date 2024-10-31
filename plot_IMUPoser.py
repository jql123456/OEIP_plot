import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    "SFU": [31321.43556, 29032.125, 18031.10889, 16931.63673, 15139.80321,
            970546.5703, 991291.9922, 1068938.438, 1134169.734, 701069.836],
    "MPI_mosh": [9959.32104, 10841.69091, 2123.06928, 2410.15008, 7548.63063,
                 550965.1289, 549282.6914, 620119.4765, 550740.2695, 383715.9844],
    "TotalCapture": [57181.18359, 49842.84375, 24950.08593, 27894.00585, 24991.36524,
                     2636625.094, 2764138.219, 2700726.188, 3001512.375, 1907505.703]
})

column_sums = data.sum()
normalized_data = data / column_sums

fig, ax = plt.subplots(figsize=(12, 6))
width = 0.25
x = np.arange(len(normalized_data)) + 1

ax.bar(x - width, normalized_data["SFU"], width=width, label="SFU")
ax.bar(x, normalized_data["MPI_mosh"], width=width, label="MPI_mosh")
ax.bar(x + width, normalized_data["TotalCapture"], width=width, label="TotalCapture")

ax.set_yscale('log')
ax.set_ylim(1e-3, 1)
ax.set_xlabel('Index')
ax.set_ylabel('Log Normalized Score')
ax.set_title('Normalized Scores for Each Dataset with Logarithmic Y-Axis (Bar Chart)')
ax.legend()
ax.grid(True, which="both", ls="--")
ax.set_xticks(x)
ax.set_xticklabels(x)

plt.show()
