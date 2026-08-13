# ============================================
# 问题二、三：热解产物收率实验数据与理论计算值对比图
# 2024年第九届"数维杯"大学生数学建模挑战赛 B题
# 说明：本文件为 MATLAB 代码的 Python 版本
# ============================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("问题二、三：热解产物收率实验数据与理论计算值对比图")
print("=" * 60)

# ============================================
# 数据定义
# ============================================
ratios = ['100/0', '0/100', '5/100', '10/100', '20/100', '30/100', '50/100']
x_positions = [0, 1, 2, 3, 4, 5, 6]  # 用于绘图的位置

def plot_comparison(ratios, x_pos, tar_exp, tar_calc, hex_exp, hex_calc, 
                    water_exp, water_calc, char_exp, char_calc, 
                    title, save_name):
    """
    绘制热解产物收率对比图
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # 绘制 Tar
    ax.plot(x_pos, tar_exp, '-o', color='#1f77b4', linewidth=2, 
            markersize=8, label='Tar 实验值')
    ax.plot(x_pos, tar_calc, '--^', color='#1f77b4', linewidth=2, 
            markersize=8, label='Tar 计算值')
    
    # 绘制 HEX
    ax.plot(x_pos, hex_exp, '-s', color='#ff7f0e', linewidth=2, 
            markersize=8, label='HEX 实验值')
    ax.plot(x_pos, hex_calc, '--s', color='#ff7f0e', linewidth=2, 
            markersize=8, label='HEX 计算值')
    
    # 绘制 Water
    ax.plot(x_pos, water_exp, '-d', color='#2ca02c', linewidth=2, 
            markersize=8, label='Water 实验值')
    ax.plot(x_pos, water_calc, '--d', color='#2ca02c', linewidth=2, 
            markersize=8, label='Water 计算值')
    
    # 绘制 Char
    ax.plot(x_pos, char_exp, '-p', color='#d62728', linewidth=2, 
            markersize=8, label='Char 实验值')
    ax.plot(x_pos, char_calc, '--p', color='#d62728', linewidth=2, 
            markersize=8, label='Char 计算值')
    
    ax.set_xlabel('混合比例 (生物质/煤)', fontsize=14)
    ax.set_ylabel('产物收率 (wt%, daf)', fontsize=14)
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(ratios)
    ax.legend(loc='best', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'../results/figures/{save_name}.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"  图片已保存: results/figures/{save_name}.png")

# ============================================
# 图1：木屑/黑山煤(SD/HS)
# ============================================
print("\n【1】绘制 木屑/黑山煤(SD/HS) 对比图...")

tar_exp = [27.29, 11.78, 12.77, 12.99, 14.86, 15.78, 15.87]
tar_calc = [np.nan, np.nan, 12.52, 13.19, 14.37, 15.36, 16.95]

hex_exp = [9.43, 8.18, 10.08, 10.97, 11.78, 11.97, 12.46]
hex_calc = [np.nan, np.nan, 8.24, 8.29, 8.39, 8.47, 8.6]

water_exp = [23.8, 6.1, 7.95, 8.06, 8.76, 10.07, 13]
water_calc = [np.nan, np.nan, 6.94, 7.71, 9.05, 10.18, 12]

char_exp = [28.95, 73.92, 69.49, 69.11, 64.56, 61.82, 57.44]
char_calc = [np.nan, np.nan, 71.78, 69.83, 66.43, 63.54, 58.93]

plot_comparison(
    ratios, x_positions,
    tar_exp, tar_calc,
    hex_exp, hex_calc,
    water_exp, water_calc,
    char_exp, char_calc,
    '木屑/黑山煤(SD/HS): 热解产物收率实验数据与理论计算值',
    'SD_HS_对比图'
)

# ============================================
# 图2：木屑/神木煤(SD/SM)
# ============================================
print("\n【2】绘制 木屑/神木煤(SD/SM) 对比图...")

tar_exp = [27.29, 9.01, 9.93, 10.41, 12.59, 14.22, 14.44]
tar_calc = [np.nan, np.nan, 9.88, 10.67, 12.06, 13.23, 15.1]

hex_exp = [9.43, 8.08, 8.73, 8.74, 10.75, 10.75, 10.13]
hex_calc = [np.nan, np.nan, 8.14, 8.2, 8.31, 8.39, 8.53]

water_exp = [23.8, 5.53, 6.06, 7.27, 7.06, 7.63, 11.01]
water_calc = [np.nan, np.nan, 6.4, 7.19, 8.58, 9.75, 11.62]

char_exp = [28.95, 75.68, 73.55, 71.41, 67.97, 64.69, 59.8]
char_calc = [np.nan, np.nan, 73.45, 71.43, 67.89, 64.9, 60.1]

plot_comparison(
    ratios, x_positions,
    tar_exp, tar_calc,
    hex_exp, hex_calc,
    water_exp, water_calc,
    char_exp, char_calc,
    '木屑/神木煤(SD/SM): 热解产物收率实验数据与理论计算值',
    'SD_SM_对比图'
)

print("\n" + "=" * 60)
print("问题二、三运行完成！")
print("结果图片已保存到: results/figures/")
print("=" * 60)