def max_subseq_sum3(A):
    max_sum = 0
    this_sum = 0
    for i in range(len(A)):
        this_sum += A[i]
        if this_sum > max_sum:
            max_sum = this_sum
        elif this_sum < 0: # 加负数会让和变小
            this_sum = 0
    return max_sum

# 测试
arr = [-2, 11, -4, 13, -5, -2]
print("最大子列和:", max_subseq_sum3(arr))  # 输出：20
