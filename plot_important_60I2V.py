import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    x_index = ['accel20', 'accel21', 'accel1', 'accel2', 'accel15', 'ori20', 'ori21', 'ori1', 'ori2', 'ori15']
    y_SFU = np.array(
        [3466239.25,3759434.75,1040048.188,984227.5625,1519907.625,2800704.75,2907593.25,3496457,3428270.5,2050462.375])
    y_mosh = np.array(
        [1477077.5,1453081.75,170578.9375,164529.8594,652094.9375,1210865.25,1209459.625,1108817,989240.125,721768.0625])
    y_Tc = np.array(
        [5589484.5,5696590.5,1462452.625,1389980.75,2636435.25,6441805,6283761.5,7369505.5,7793634,5169858.5])
    fig, ax = plt.subplots(figsize=(16, 4))
    x = np.arange(len(x_index))
    bar_width = 0.3
    bars1 = ax.bar(x - 0.3, y_SFU / max(y_SFU), width=bar_width, label='SFU', color='#41A8BF')
    bars2 = ax.bar(x, y_mosh / max(y_mosh), width=bar_width, label='MPI_mosh', color='#B0D1D9')
    bars3 = ax.bar(x + 0.3, y_Tc / max(y_Tc), width=bar_width, label='TotalCapture', color='#F2B077')
    ax.set_xticks(x)
    ax.set_xticklabels(x_index, rotation=45, ha='right')

    ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))

    ax.set_title("Importance of Each Input Type")
    ax.set_xlabel("Input Type")
    ax.set_ylabel("Importance")
    plt.subplots_adjust(right=0.8, bottom=0.3)

    plt.savefig("60I2V_global_captum.pdf", bbox_inches='tight')
