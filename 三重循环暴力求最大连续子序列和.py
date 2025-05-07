def max_subseq_sum1(A):
    N = len(A)
    max_sum = 0
    for i in range(N):         # i 是子列左端
        for j in range(i, N):  # j 是子列右端
            this_sum = 0
            for k in range(i, j + 1):  # 遍历 A[i] 到 A[j]
                this_sum += A[k]
            if this_sum > max_sum:
                max_sum = this_sum

    return max_sum


# 测试
arr=[-2,11,-4,13,-5,-2] # 6
print(f"三重循环暴力算法求最大子列和：{max_subseq_sum1(arr)}")

