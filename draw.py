import matplotlib.pyplot as plt

# 示例数据
x = [3, 4, 8, 12, 16, 20]
y = [84.3, 85.0, 85.5, 85.3, 84.7, 84.3]

# baseline 精度
baseline_accuracy = 83.7

# 画折线图
plt.plot(x, y, marker='o', label='Model Accuracy')

# 添加 baseline 虚线
plt.axhline(y=baseline_accuracy, color='r', linestyle='--', label='Baseline Accuracy')

# 添加标题和标签
plt.title("Results on PACS")
plt.xlabel("Cluster number")
plt.ylabel("Accuracy")

# 指定要标注的点
x_target = 3
y_target = y[0]  # 获取 x=3 对应的 y 值

# 在 (x_target, y_target) 处添加标注
plt.annotate(
    f'x={x_target}',                   # 显示 x 值
    (x_target, y_target),              # 标注位置
    textcoords="offset points",        # 文字偏移
    xytext=(0, 10),                    # 标注偏移量
    ha='center',                       # 水平对齐方式
    # arrowprops=dict(arrowstyle="->", color='black')  # 箭头样式
)


# 显示图例
plt.legend()

# 显示图形
# plt.show()

plt.savefig("PACS.pdf", format='pdf', dpi=300)