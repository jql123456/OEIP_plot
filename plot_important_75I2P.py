import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    # x_index = ['accel20', 'accel21', 'accel1', 'accel2', 'accel15', 'ori20', 'ori21', 'ori1', 'ori2', 'ori15', 'velocity20', 'velocity21', 'velocity1', 'velocity2', 'velocity15']
    x_index = ['accel20', 'accel21', 'accel1', 'accel2', 'accel15', 'ori20', 'ori21', 'ori1', 'ori2', 'ori15']
    # y_SFU = np.array(
    #     [11149192,10514900,4214742,3779680.5,3647677.25,45968392,49476148,50115492,47453432,26804368])
    y_SFU = np.array(
        [32440080,7483084.5,34090644,6526063,38838316,2751890,66149404,2549204,18321772,2387487.75])

    y_mosh = np.array(
        [20874660,4412867,19288368,3894600.75,18925580.22,683704.75,20251716,678865.8125,9831132,1432542.875])
    y_Tc = np.array(
        [21787000,19661000,7189500,5810100,7088300,138340000,141610000,129910000,127260000,72222000])
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


