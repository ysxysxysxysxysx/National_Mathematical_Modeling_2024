# ============================================
# 问题1：正己烷不溶物(INS)与热解产率的散点回归图
# 2024年第九届"数维杯"大学生数学建模挑战赛 B题
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from scipy.interpolate import make_interp_spline

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_excel('附件一.xlsx')
df.fillna(0, inplace=True)

sns.set_style("whitegrid")

# ============================================
# 图1：INS vs 焦油产率
# ============================================
x = df['正己烷不溶物（INS)g'].values.reshape(-1, 1)
y = df['焦油产率'].values
model = LinearRegression().fit(x, y)
x_range = np.linspace(x.min(), x.max(), 300).reshape(-1, 1)
y_range_pred = model.predict(x_range)

# 创建平滑曲线
spl = make_interp_spline(x_range.squeeze(), y_range_pred)
x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = spl(x_smooth)

plt.figure(figsize=(10, 6))
sns.kdeplot(x=df['正己烷不溶物（INS)g'], y=df['焦油产率'], levels=5, color="b", fill=True, alpha=0.5)
plt.plot(x_smooth, y_smooth, color="r", label='回归曲线')
plt.legend()
plt.title('正己烷不溶物（INS)与焦油产率关系')
plt.xlabel('正己烷不溶物（INS)g')
plt.ylabel('焦油产率')
plt.show()

# ============================================
# 图2：INS vs 水产率
# ============================================
x = df['正己烷不溶物（INS)g'].values.reshape(-1, 1)
y = df['水产率'].values
model = LinearRegression().fit(x, y)
x_range = np.linspace(x.min(), x.max(), 300).reshape(-1, 1)
y_range_pred = model.predict(x_range)

spl = make_interp_spline(x_range.squeeze(), y_range_pred)
x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = spl(x_smooth)

plt.figure(figsize=(10, 6))
sns.kdeplot(x=df['正己烷不溶物（INS)g'], y=df['水产率'], levels=5, color="b", fill=True, alpha=0.5)
plt.plot(x_smooth, y_smooth, color="r", label='回归曲线')
plt.legend()
plt.title('正己烷不溶物（INS)与水产率关系')
plt.xlabel('正己烷不溶物（INS)g')
plt.ylabel('水产率')
plt.show()

# ============================================
# 图3：INS vs 焦渣产率
# ============================================
x = df['正己烷不溶物（INS)g'].values.reshape(-1, 1)
y = df['焦渣产率'].values
model = LinearRegression().fit(x, y)
x_range = np.linspace(x.min(), x.max(), 300).reshape(-1, 1)
y_range_pred = model.predict(x_range)

spl = make_interp_spline(x_range.squeeze(), y_range_pred)
x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = spl(x_smooth)

plt.figure(figsize=(10, 6))
sns.kdeplot(x=df['正己烷不溶物（INS)g'], y=df['焦渣产率'], levels=5, color="b", fill=True, alpha=0.5)
plt.plot(x_smooth, y_smooth, color="r", label='回归曲线')
plt.legend()
plt.title('正己烷不溶物（INS)与焦渣产率关系')
plt.xlabel('正己烷不溶物（INS)g')
plt.ylabel('焦渣产率')
plt.show()