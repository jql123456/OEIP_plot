import torch
import torch.nn as nn
from captum.attr import FeatureAblation
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. 定义简单的时序回归模型
class SimpleTimeSeriesModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1):
        super(SimpleTimeSeriesModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out)
        return out


# 模型参数
input_size = 10
hidden_size = 20
output_size = 5
num_layers = 2

# 创建模型实例
model = SimpleTimeSeriesModel(input_size, hidden_size, output_size, num_layers)
model.eval()

# 2. 生成示例时序数据
seq_len = 50
batch_size = 1

torch.manual_seed(0)
input_tensor = torch.randn(batch_size, seq_len, input_size, requires_grad=True)
output_tensor = torch.randn(batch_size, seq_len, output_size)

# 3. 使用 Feature Ablation 进行特征重要性评估
feature_ablation = FeatureAblation(model)

with torch.no_grad():
    output = model(input_tensor)

ablation_attr = feature_ablation.attribute(input_tensor, target=None)
attr = ablation_attr.squeeze().detach().numpy()  # [seq_len, input_size]

# 4a. 可视化热力图
features = [f'特征 {i + 1}' for i in range(input_size)]
#
# plt.figure(figsize=(14, 8))
# sns.heatmap(attr.T, cmap='coolwarm', xticklabels=10, yticklabels=features, cbar=True)
# plt.xlabel('时间步')
# plt.ylabel('输入特征')
# plt.title('Feature Ablation 评分热力图')
# plt.show()

# 4b. 可视化折线图
# plt.figure(figsize=(14, 8))
#
# for feature_idx in range(input_size):
#     plt.plot(range(seq_len), attr[:, feature_idx], label=f'特征 {feature_idx + 1}')
#
# plt.xlabel('时间步')
# plt.ylabel('Feature Ablation 评分')
# plt.title('Feature Ablation 评分随时间变化的折线图')
# plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
# plt.tight_layout()
# plt.show()

# 4c. 可视化聚合评分
average_attr = np.mean(attr, axis=0)  # [input_size]

plt.figure(figsize=(12, 6))
bars = plt.bar(features, average_attr, color='skyblue')
plt.xlabel('输入特征')
plt.ylabel('平均 Feature Ablation 评分')
plt.title('各输入特征的平均 Feature Ablation 评分')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.2f}', ha='center', va='bottom')

plt.show()
