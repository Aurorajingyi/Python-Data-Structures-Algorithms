def evaluate_direct(coeffs, x):  # coefficients系数
    # 系数从小到大:1 + 2x + 3x²
    result = 0
    for i in range(len(coeffs)):
        result += coeffs[i] * (x ** i)
    return result


# # 测试：多项式 1 + 2x + 3x² 在 x=2 处的值
print(evaluate_direct([1, 2, 3], 2))


# Horner法则

def evaluate_horner(coeffs, x):
    result = 0
    for coeff in reversed(coeffs):  # 直接返回迭代器不生成新列表（内存友好）
        result = result * x + coeff  # result = an
    return result  # result = anx+ a^(n-1)


print(evaluate_horner([1, 2, 3], 2))
