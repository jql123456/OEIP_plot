import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    "SFU": [23052333, 19453731, 13177686, 12214892.25, 9848968.5,
            287317656, 297438516, 348046092, 594118008, 161347140],
    "MPI_mosh": [13107565.5, 11600041.5, 4103614.5, 4582641, 6814727.25,
                 179228970, 167712426, 169250940, 178712802, 84925602],
    "TC": [38208339, 34759812, 17408572.5, 15918841.5, 14809450.5,
           882388440, 961815672, 945361080, 2127584160, 368762688]
})

column_sums = data.sum()
normalized_data = data / column_sums

fig, ax = plt.subplots(figsize=(12, 6))
width = 0.25
x = np.arange(len(normalized_data)) + 1

ax.bar(x - width, normalized_data["SFU"], width=width, label="SFU")
ax.bar(x, normalized_data["MPI_mosh"], width=width, label="MPI_mosh")
ax.bar(x + width, normalized_data["TC"], width=width, label="TC")

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
