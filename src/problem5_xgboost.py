# ============================================
# 问题五：基于 XGBoost 的热解产物产率预测模型
# 2024年第九届"数维杯"大学生数学建模挑战赛 B题
# 包含：数据加载、模型训练、预测、可视化对比图
# ============================================

import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("问题五：XGBoost 热解产物产率预测模型")
print("=" * 60)

# ============================================
# 1. 加载数据
# ============================================
print("\n【1】加载数据...")

# 注意：请将附件一.xlsx 放在 data/raw/ 目录下
# 或者修改为你的实际文件路径
df = pd.read_excel('../data/raw/附件一.xlsx')
df.fillna(0, inplace=True)

print(f"  数据形状: {df.shape}")
print(f"  列名: {df.columns.tolist()}")

# ============================================
# 2. 准备训练数据
# ============================================
print("\n【2】准备训练数据...")

# 特征列（自变量）
feature_cols = ['样品g', '配比计算', '正己烷不溶物（INS)g']
# 目标列（因变量）
target_cols = ['焦油产率', '水产率', '焦渣产率', '正己烷可溶物产率']

# 检查列名是否匹配，如果不匹配则尝试常见变体
actual_cols = df.columns.tolist()
for col in feature_cols + target_cols:
    if col not in actual_cols:
        print(f"  警告: 列 '{col}' 不存在，请检查数据文件列名")
        print(f"  实际列名: {actual_cols}")
        exit()

X = df[feature_cols]
y = df[target_cols]

print(f"  特征: {feature_cols}")
print(f"  目标: {target_cols}")
print(f"  样本数: {len(X)}")

# ============================================
# 3. 划分训练集和测试集
# ============================================
print("\n【3】划分训练集和测试集 (80% / 20%)...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"  训练集: {X_train.shape[0]} 样本")
print(f"  测试集: {X_test.shape[0]} 样本")

# ============================================
# 4. 训练 XGBoost 模型
# ============================================
print("\n【4】训练 XGBoost 模型...")

# 构建 DMatrix 格式
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test)

# 设置参数
params = {
    'objective': 'reg:squarederror',
    'learning_rate': 0.1,
    'max_depth': 6,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'seed': 42
}

print(f"  参数: {params}")

# 训练模型
model = xgb.train(
    params, 
    dtrain, 
    num_boost_round=100,
    verbose_eval=False
)

print("  模型训练完成！")

# ============================================
# 5. 预测
# ============================================
print("\n【5】生成预测结果...")

y_pred_train = model.predict(xgb.DMatrix(X_train))
y_pred_test = model.predict(xgb.DMatrix(X_test))

print(f"  训练集预测完成: {y_pred_train.shape}")
print(f"  测试集预测完成: {y_pred_test.shape}")

# ============================================
# 6. 绘制对比图
# ============================================
print("\n【6】生成预测值 vs 实际值对比图...")

def plot_comparison(y_true, y_pred, target_name, save_path=None):
    """
    绘制预测值 vs 实际值的散点对比图
    """
    plt.figure(figsize=(10, 8))
    
    # 训练集散点图
    plt.scatter(
        y_true, 
        y_pred, 
        alpha=0.5, 
        color='red', 
        label='预测值',
        s=60
    )
    
    # 添加对角线参考线 (y=x)
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    plt.plot(
        [min_val, max_val], 
        [min_val, max_val], 
        'k--', 
        lw=2, 
        label='y = x (完美预测)'
    )
    
    plt.title(f'{target_name} 预测值 vs 实际值', fontsize=16, fontweight='bold')
    plt.xlabel('实际值', fontsize=14)
    plt.ylabel('预测值', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"  图片已保存: {save_path}")
    
    plt.show()

# 遍历每个目标变量，分别绘制
for i, target in enumerate(target_cols):
    # 使用测试集数据
    y_true = y_test[target].values
    y_pred = y_pred_test[:, i]
    
    # 计算 R² 和 RMSE
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    
    print(f"\n  {target}:")
    print(f"    R² = {r2:.4f}")
    print(f"    RMSE = {rmse:.4f}")
    
    # 保存图片到 results/figures/
    save_path = f'../results/figures/{target}_对比图.png'
    plot_comparison(y_true, y_pred, target, save_path)

# ============================================
# 7. 特征重要性分析
# ============================================
print("\n【7】特征重要性分析...")

importance = model.get_score(importance_type='weight')
importance_dict = {feature_cols[int(k[1:])]: v for k, v in importance.items()}
sorted_importance = sorted(importance_dict.items(), key=lambda x: x[1], reverse=True)

print("  特征重要性排序:")
for i, (feature, score) in enumerate(sorted_importance, 1):
    print(f"    {i}. {feature}: {score}")

# 绘制特征重要性图
plt.figure(figsize=(8, 6))
features = [item[0] for item in sorted_importance]
scores = [item[1] for item in sorted_importance]
plt.barh(features, scores, color='steelblue')
plt.xlabel('重要性得分', fontsize=12)
plt.title('XGBoost 特征重要性', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('../results/figures/特征重要性.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n" + "=" * 60)
print("问题五运行完成！")
print("结果图片已保存到: results/figures/")
print("=" * 60)