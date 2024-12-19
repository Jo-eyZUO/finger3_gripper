# %%

ids = [[2], [1]]
print(ids[1][0])
# 查找元素 [2] 的索引
index = next((idx for idx, sublist in enumerate(ids) if [2] in sublist), None)

if index is not None:
    print(f"元素 [2] 的索引是：{index}")
else:
    print("未找到元素 [2]")

# %%
my_list = [10, 20, 30, 40, 50]

# 查找元素的索引
element = 30
idx = my_list.index(element)

print(f"元素 {element} 的索引是：{idx}")
# %%
import numpy as np

pos_1 = [0, 0]
pos_2 = [0, 0]
pos_3 = [0, 0]
ids = np.array([[1],[0]])
print(f'ids, {ids}')
corners=([[[1030., 1279.],
        [ 960., 1278.],
        [ 963., 1253.],
        [1025., 1252.]]], 
        [[[542., 557.],
        [576., 496.],
        [593., 510.],
        [562., 564.]]])
if len(ids) > 0:
    for id in ids:
        indices = np.where(ids == id)[0][0]
        # print(f' np.where(ids == id), { np.where(ids == id)}')
        print(f'indices, {indices}')
        if id == [0]:
            pos_1 = corners[indices][0][0]
        if id == [1]:
            pos_2 = corners[indices][0][0]
        if id == [2]:
            pos_3 = corners[indices][0][0]   
# print(f'pos_1, {pos_1}')
# print(f'pos_2, {pos_2}')
# print(f'pos_3, {pos_3}')


# 定义两个坐标点
pos_1 = np.array(pos_1)
pos_2 = np.array(pos_2)
pos_3 = np.array(pos_3)

# 计算两个点之间的欧氏距离
dis_12 = np.linalg.norm(pos_1 - pos_2)
dis_13 = np.linalg.norm(pos_1 - pos_3)
dis_23 = np.linalg.norm(pos_2 - pos_3)

print(f'dis_12, {dis_12}')
print(f'dis_13, {dis_13}')
print(f'dis_23, {dis_23}')
diff1213 = abs(dis_12-dis_13)
diff1223 = abs(dis_12-dis_23)
diff1323 = abs(dis_13-dis_23)
print(f'diff1213, {diff1213}')
print(f'diff1223, {diff1223}')
print(f'diff1323, {diff1323}')
if diff1213 < 10 and diff1223 < 10 and diff1323 < 10:
    print("<<<<<<<< success")
else:
    print("绝对值之差不小于10")
# %%
import numpy as np

# 创建一个 NumPy 数组
arr = np.array([[30], [40], [50]])

# 要查找的值
value = [40]

# 使用 np.where() 函数查找值的索引
indices = np.where(arr == value)[0]

if len(indices) > 0:
    print(f"值 {value} 的索引是：{indices}")
else:
    print(f"值 {value} 未找到")
# %%
