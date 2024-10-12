import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    x_index = ['accel20', 'accel21', 'accel1', 'accel2', 'accel15', 'ori20', 'ori21', 'ori1', 'ori2', 'ori15']
    y_SFU = np.array([859.55334,982.51294,508.07547,564.13,281.82556,41491.66797,53807.52734,26948.51172,65975.96875,27151.4707])
    y_mosh = np.array([137.78938,297.85828,31.76596,33.56823,44.53313,22305.21484,29566.64844,35585.12891,8583.69434,8485.99707])
    y_Tc = np.array([1062.12134,1109.34924,458.0603,2003.93127,200.23221,136070.1875,145995.8299,39372.26172,253818.1406,115832.5469])

    fig, ax = plt.subplots(figsize=(16, 4))
    x = np.arange(len(x_index))
    bar_width = 0.3
    bars1 = ax.bar(x - 0.3, y_SFU/max(y_SFU), width=bar_width, label='SFU', color='#41A8BF')
    bars2 = ax.bar(x, y_mosh/max(y_mosh), width=bar_width, label='MPI_mosh', color='#B0D1D9')
    bars3 = ax.bar(x + 0.3, y_Tc/max(y_Tc), width=bar_width, label='TotalCapture', color='#F2B077')

    ax.set_xticks(x)
    ax.set_xticklabels(x_index, rotation=45, ha='right')

    ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))

    ax.set_title("Importance of Each Input Type")
    ax.set_xlabel("Input Type")
    ax.set_ylabel("Importance")
    plt.subplots_adjust(right=0.8, bottom=0.3)

    plt.savefig("60_global_captum.pdf", bbox_inches='tight')

    plt.show()
