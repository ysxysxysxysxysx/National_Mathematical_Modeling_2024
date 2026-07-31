# ============================================
# 问题1：正己烷不溶物(INS)对热解产率的影响分析
# 方法：Pearson / Spearman / Kendall 相关系数分析
# 2024年第九届"数维杯"大学生数学建模挑战赛 B题
# 说明：本文件为 MATLAB 代码的 Python 版本
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("问题1：正己烷不溶物(INS)对热解产率的影响分析")
print("=" * 60)

# ============================================
# 1. 数据提取和异常数据处理
# ============================================
print("\n【1】加载数据...")

# 读取数据（请将文件放在 data/raw/ 目录下）
df = pd.read_excel('../data/raw/附件一热解数据统计改英文表头版本.xlsx')

# 提取需要的列（根据实际列名调整）
insg = df['INSg'].values
charyita = df['Charyita'].values
wateryita = df['Wateryita'].values
pcharyita = df['Pcharyita'].values

# 将 INS 缺失值替换为 0
insg = np.nan_to_num(insg, nan=0)
js = np.isnan(df['INSg']).sum()

# 构建数据矩阵（从第2行开始）
bsdata = np.column_stack([
    insg[1:], 
    charyita[1:], 
    wateryita[1:], 
    pcharyita[1:]
])

# 数据归一化到 [0, 1]
scaler = MinMaxScaler()
bsdataf = scaler.fit_transform(bsdata)

print(f"  数据形状: {bsdataf.shape}")
print(f"  INS 缺失值数量: {js}")

# ============================================
# 2. 计算三种相关系数
# ============================================
print("\n【2】计算相关系数矩阵...")

# Pearson 相关系数
rho_pearson = np.corrcoef(bsdataf.T)

# Spearman 相关系数
rho_spearman, _ = stats.spearmanr(bsdataf)

# Kendall 相关系数
rho_kendall, _ = stats.kendalltau(bsdataf[:, 0], bsdataf[:, 1])
# Kendall 需要逐对计算，这里简化处理
rho_kendall_matrix = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        rho_kendall_matrix[i, j], _ = stats.kendalltau(bsdataf[:, i], bsdataf[:, j])

string_name = ['正己烷不溶物(INS)', '焦油产率', '水产率', '焦渣产率']

print("\n  Pearson 相关系数矩阵:")
print(pd.DataFrame(rho_pearson, index=string_name, columns=string_name).round(4))

print("\n  Spearman 相关系数矩阵:")
print(pd.DataFrame(rho_spearman, index=string_name, columns=string_name).round(4))

print("\n  Kendall 相关系数矩阵:")
print(pd.DataFrame(rho_kendall_matrix, index=string_name, columns=string_name).round(4))

# ============================================
# 3. 绘制热力图
# ============================================
print("\n【3】绘制热力图...")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 绘制 Pearson 相关系数矩阵
sns.heatmap(
    rho_pearson, 
    annot=True, 
    fmt='.3f', 
    xticklabels=string_name, 
    yticklabels=string_name,
    cmap='summer', 
    center=0,
    ax=axes[0]
)
axes[0].set_title('Pearson 相关系数矩阵', fontsize=14)

# 绘制 Spearman 相关系数矩阵
sns.heatmap(
    rho_spearman, 
    annot=True, 
    fmt='.3f', 
    xticklabels=string_name, 
    yticklabels=string_name,
    cmap='summer', 
    center=0,
    ax=axes[1]
)
axes[1].set_title('Spearman 相关系数矩阵', fontsize=14)

# 绘制 Kendall 相关系数矩阵
sns.heatmap(
    rho_kendall_matrix, 
    annot=True, 
    fmt='.3f', 
    xticklabels=string_name, 
    yticklabels=string_name,
    cmap='summer', 
    center=0,
    ax=axes[2]
)
axes[2].set_title('Kendall 相关系数矩阵', fontsize=14)

plt.tight_layout()
plt.savefig('../results/figures/相关系数矩阵.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n" + "=" * 60)
print("问题1运行完成！")
print("结果图片已保存到: results/figures/相关系数矩阵.png")
print("=" * 60)