import numpy as np
import matplotlib.pyplot as plt


# 加载数据
OEIP3_data = np.loadtxt(open("CDF_datas/all/OEIP3joints.csv", "rb"), delimiter=",", skiprows=0)
IMUPoser3_data = np.loadtxt(open("CDF_datas/all/IMUPoser3joints.csv", "rb"), delimiter=",", skiprows=0)
OEIP2_data = np.loadtxt(open("CDF_datas/all/OEIP2joints.csv", "rb"), delimiter=",", skiprows=0)
IMUPoser2_data = np.loadtxt(open("CDF_datas/all/IMUPoser2joints.csv", "rb"), delimiter=",", skiprows=0)
OEIP1_data = np.loadtxt(open("CDF_datas/all/OEIP1joint.csv", "rb"), delimiter=",", skiprows=0)
IMUPoser1_data = np.loadtxt(open("CDF_datas/all/IMUPoser1joint.csv", "rb"), delimiter=",", skiprows=0)



# selected_indices = 0
OEIP3_selected = OEIP3_data
IMUPoser3_selected = IMUPoser3_data
OEIP2_selected = OEIP2_data
IMUPoser2_selected = IMUPoser2_data
OEIP1_selected = OEIP1_data
IMUPoser1_selected = IMUPoser1_data


OEIP3_selected_sorted = np.sort(OEIP3_selected, axis=0)
IMUPoser3_selected_sorted = np.sort(IMUPoser3_selected, axis=0)
OEIP2_selected_sorted = np.sort(OEIP2_selected, axis=0)
IMUPoser2_selected_sorted = np.sort(IMUPoser2_selected, axis=0)
OEIP1_selected_sorted = np.sort(OEIP1_selected, axis=0)
IMUPoser1_selected_sorted = np.sort(IMUPoser1_selected, axis=0)

cdf_OEIP3 = np.arange(1, len(OEIP3_selected_sorted)+1) / len(OEIP3_selected_sorted)
cdf_IMUPoser3 = np.arange(1, len(IMUPoser3_selected_sorted)+1) / len(IMUPoser3_selected_sorted)
cdf_OEIP2 = np.arange(1, len(OEIP2_selected_sorted)+1) / len(OEIP2_selected_sorted)
cdf_IMUPoser2 = np.arange(1, len(IMUPoser2_selected_sorted)+1) / len(IMUPoser2_selected_sorted)
cdf_OEIP1 = np.arange(1, len(OEIP1_selected_sorted)+1) / len(OEIP1_selected_sorted)
cdf_IMUPoser1 = np.arange(1, len(IMUPoser1_selected_sorted)+1) / len(IMUPoser1_selected_sorted)


# 绘制CDF曲线
plt.figure(figsize=(8, 6))
plt.plot(OEIP3_selected_sorted, cdf_OEIP3, marker='.', linestyle='none', color='#41A8BF', label='OEIP3Joints')
plt.plot(IMUPoser3_selected_sorted, cdf_IMUPoser3, marker='.', linestyle='none', color='#B0D1D9', label='IMUPoser3Joints')
plt.plot(OEIP2_selected_sorted, cdf_OEIP2, marker='.', linestyle='none', color='#F2B077', label='OEIP2Joints')
plt.plot(IMUPoser2_selected_sorted, cdf_IMUPoser2, marker='.', linestyle='none', label='IMUPoser2Joints')
plt.plot(OEIP1_selected_sorted, cdf_OEIP1, marker='.', linestyle='none', label='OEIP1Joints')
plt.plot(IMUPoser1_selected_sorted, cdf_IMUPoser1, marker='.', linestyle='none', label='IMUPoser1Joints')
plt.legend(loc='center right')
plt.xlabel('')
plt.ylabel('CDF')
plt.title('CDF Performance')
plt.grid(True)
plt.show()

