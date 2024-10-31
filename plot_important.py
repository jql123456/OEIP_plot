import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    x_index = ['accel20', 'accel21', 'accel1', 'accel2', 'accel15', 'ori20', 'ori21', 'ori1', 'ori2', 'ori15']
    # y_TC1 = np.array(
    #     [23051836.5,19453422,13178145,12214757.25,9848188.5,287316684,297439020,348048896,594108972,161339292])
    # y_TC1 = np.array(
    #     [13107240,11599746.75,4103580,4582520.625,6814473.75,179223138,167712066,169255044,178716942,84925890])
    y_TC1 = np.array(
        [38208000,34761000,17407800,15918000,14809200,882396000,961830000,945360000,2127510000,368766000], dtype=float)
    # y_TC2 = np.array(
    #     [19058.79883,16611.74609,8312.90137,9296.38281,8326.44238,292951.5,307131.7813,300060.375,333497.5,211941.8594])
    # y_TC2 = np.array(
    #     [3318.86841,3613.10205,705.26312,802.06042,2516.40942,61223.10938,61032.2066,68899.3125,61192.70312,42635.75781])
    y_TC2 = np.array(
        [10441.30762,9677.47754,6008.86865,5641.37891,5046.45117,107838.9297,110144.0547,118766.0078,126019.8984,77895.16406])
    y_TC1[5:] /= 3.0
    y_TC2[5:] /= 3.0

    scale1 = np.sum(y_TC1)/5
    scale2 = np.sum(y_TC2)/5

    fig, ax = plt.subplots(figsize=(16, 4))
    x = np.arange(len(x_index))
    bar_width = 0.3
    bars1 = ax.bar(x - 0.3, y_TC1 / scale1, width=bar_width, label='SFU', color='#41A8BF')
    bars2 = ax.bar(x, y_TC2 / scale2, width=bar_width, label='MPI_mosh', color='#B0D1D9')
    ax.set_xticks(x)
    ax.set_xticklabels(x_index, rotation=45, ha='right')

    ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))

    ax.set_title("Importance of Each Input Type")
    ax.set_xlabel("Input Type")
    ax.set_ylabel("Importance")
    plt.subplots_adjust(right=0.8, bottom=0.3)
    plt.show()
    # plt.savefig("60I2V_global_captum.pdf", bbox_inches='tight')
