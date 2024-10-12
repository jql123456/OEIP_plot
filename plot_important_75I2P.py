import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    x_index = ['accel20', 'accel21', 'accel1', 'accel2', 'accel15', 'ori20', 'ori21', 'ori1', 'ori2', 'ori15', 'velocity20', 'velocity21', 'velocity1', 'velocity2', 'velocity15']
    y_SFU = np.array(
        [1431037.125,1457524.125,2360471.75,2208539.75,1526351.875,43532108,46932824,23870042,24626680,20024812,12099465,12453354,9066306,9031851,10166796])
    y_mosh = np.array(
        [626771.8125,587390.375,318243.0625,303955.2188,602555.8125,25773606,25927182,14841812,15009380,12602982,5965749,6222107,267528.5313,297861.4688,3309238.25])
    y_Tc = np.array(
        [2422806,2332808.75,2607729.5,2569993.75,2038477.625,128635320,135432784,65697828,66295432,59976376,18300112,20581926,1149602.375,1313200,10482961])
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

    plt.savefig("75I2P_global_captum.pdf", bbox_inches='tight')


