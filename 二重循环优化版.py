def max_subseq_sum2(A):
    max_sum = 0
    N = len(A)
    for i in range(N):
        this_sum = 0
        for j in range(i, N):
            this_sum += A[j]
            if this_sum > max_sum:
                max_sum = this_sum
    return max_sum

# 测试
arr=[-2,11,-4,13,-5,-2] # 6
print(f"二重循环暴力算法求最大子列和：{max_subseq_sum2(arr)}")