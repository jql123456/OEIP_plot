import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 加载数据
OEIP_data = np.loadtxt(open("CDF_datas/rw_lp_rp/OEIP/cdf.csv", "rb"), delimiter=",", skiprows=0)
IMUPoser_data = np.loadtxt(open("CDF_datas/rw_lp_rp/IMUPoser/cdf.csv", "rb"), delimiter=",", skiprows=0)

joints_name = ['lw', 'rw', 'lp', 'rp', 'lf', 'rf', 'h']

# 提取指定的关节点位置误差（20，21，1，2，7，8，15）
selected_indices = [0, 1, 4, 5, 6]
OEIP_selected = OEIP_data[:, selected_indices]
IMUPoser_selected = IMUPoser_data[:, selected_indices]

# 转换为 DataFrame 并添加来源标签
df_OEIP = pd.DataFrame(OEIP_selected, columns=[f'{joints_name[i]}' for i in selected_indices])
df_OEIP['Source'] = 'OEIP'

df_IMUPoser = pd.DataFrame(IMUPoser_selected, columns=[f'{joints_name[i]}' for i in selected_indices])
df_IMUPoser['Source'] = 'IMUPoser'

# 合并数据
df = pd.concat([df_OEIP, df_IMUPoser], ignore_index=True)

# 将数据转换为长格式，便于绘制小提琴图
df_melted = df.melt(id_vars='Source', var_name='Joint', value_name='Position Error')

# 为散点图随机采样数据
sample_frac = 0.06  # 采样20%的数据
num_samples = int(len(OEIP_selected) * sample_frac)
random_indices = np.random.choice(len(OEIP_selected), num_samples, replace=False)

# 对散点图使用采样后的数据
OEIP_sampled = OEIP_selected[random_indices]
IMUPoser_sampled = IMUPoser_selected[random_indices]

# 转换为 DataFrame 并添加来源标签
df_OEIP_sampled = pd.DataFrame(OEIP_sampled, columns=[f'Joint {i}' for i in selected_indices])
df_OEIP_sampled['Source'] = 'OEIP'

df_IMUPoser_sampled = pd.DataFrame(IMUPoser_sampled, columns=[f'Joint {i}' for i in selected_indices])
df_IMUPoser_sampled['Source'] = 'IMUPoser'

# 合并采样后的数据
df_sampled = pd.concat([df_OEIP_sampled, df_IMUPoser_sampled], ignore_index=True)

# 将采样后的数据转换为长格式，便于绘制散点图
df_sampled_melted = df_sampled.melt(id_vars='Source', var_name='Joint', value_name='Position Error')

# 绘制小提琴图
fig, ax = plt.subplots(figsize=(10, 6))

# 小提琴图，使用完整数据
sns.violinplot(x='Joint', y='Position Error', data=df_melted, cut=0, scale='width',
               inner=None, linewidth=1, hue='Source', split=True, palette={'OEIP': '#41A8BF', 'IMUPoser': '#B0D1D9'})

# 叠加散点图，使用采样后的数据
sns.stripplot(x='Joint', y='Position Error', data=df_sampled_melted, hue='Source', jitter=0.25,
              dodge=True, linewidth=0.5, marker='o', alpha=0.6, palette={'OEIP': '#1f77b4', 'IMUPoser': '#ff7f0e'})

# 调整标签、标题和旋转X轴标签
plt.xlabel('Joint')
plt.ylabel('Position Error')
plt.title('Violin Plot of Position Errors(lw_rw_h))')
plt.xticks(rotation=45, ha='right')

# 去除图框的左边界
sns.despine(left=True)

# 避免重复图例
handles, labels = ax.get_legend_handles_labels()
plt.legend(handles[:2], labels[:2], title='Source', loc='upper right')
# plt.show()
plt.savefig("violin-plot-of-pe-rwlprp.pdf", bbox_inches='tight')