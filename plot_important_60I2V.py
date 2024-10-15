import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    x_index = ['accel20', 'accel21', 'accel1', 'accel2', 'accel15', 'ori20', 'ori21', 'ori1', 'ori2', 'ori15']
    y_SFU = np.array(
        [1030573.25,1037021.188,157132.7344,153160.4688,276933.25,1060047.25,1035641.75,460040,437839.875,445821.5625])
    y_mosh = np.array(
        [487278.0938,487601.625,36463.76953,34295.04297,185884.0313,534118.5625,534063.8125,153123.6406,158221.2031,248800.2344])
    y_Tc = np.array(
        [1712435.5,1738479.25,226189.8594,211498.7344,435726.25,2223599.5,2149434,801716.4861,794754.3125,886847.25])
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
