def print_n_loop(n):
    for i in range(1,n+1):
        print(i)

print_n_loop(10)

# 递归
def print_n_recursive(n):
    if n>0:
        print_n_recursive(n-1) # n > 0 是递归继续的条件，当n=0时停止递归。
        print(n)

print_n_recursive(10)
"""
调用 print_n_recursive(0)

n=0 → 不满足条件，直接返回，终止递归
开始反向执行打印（堆栈弹出）：

返回 print_n_recursive(1) 的挂起点，执行 print(1)
返回 print_n_recursive(2) 的挂起点，执行 print(2)
返回 print_n_recursive(3) 的挂起点，执行 print(3)
"""

