import numpy as np
from pulp import *

# 创建10个决策变量
x = list(map(lambda i: LpVariable(f'x{i+1}', 0, None, LpInteger), range(10)))

# 定义整数规划问题
problem = LpProblem('lp', LpMinimize)

# 定义不等式约束
A_ub = [
    [2,1,1,-1,-2,0,0,0,0,0],
    # [2,-1,-2,-1,1,2,1,1,-1,-1],
    # [0,0,0,0,0,1,2,-1,1,0],
]
b_ub = [
    2,
]
for i in range(0, len(A_ub)):
    tmp = A_ub[i][0]*x[0]
    for j in range(1, len(A_ub[i])):
        tmp = tmp + A_ub[i][j]*x[j]
    problem += tmp >= b_ub[i]

# 定义等式约束
A_eq = [
    # [2,1,1,-1,-2,0,0,0,0,0],
    [2,-1,-2,-1,1,2,1,1,-1,-1],
    [0,0,0,0,0,1,2,-1,1,0],
    [1,1,1,1,1,1,1,1,1,1],
]
b_eq = [
    # 1,
    -1,
    -1,
    4,
]
for i in range(0, len(A_eq)):
    tmp = A_eq[i][0]*x[0]
    for j in range(1, len(A_eq[i])):
        tmp = tmp + A_eq[i][j]*x[j]
    problem += tmp == b_eq[i]
# 假设价值向量均为1
c = [1,1,1,1,1,1,1,1,1,1]

# 添加目标函数
tmp = c[0]*x[0]
for j in range(1, len(c)):
    tmp = tmp + c[j]*x[j]
problem += tmp

problem.solve()

# 写入求解过程
problem.writeLP('tmp.lp')

# 打印所有的决策变量
for v in problem.variables():
    print(f'{v.name}={v.varValue}')