def max3(a,b,c):
    return max(a,b,c)

def divide_and_conquer(A,left,right): # 左端点、右端点
    if left == right:
        return A[left] if A[left]>0 else 0 # 当分到最小单位时

    center = (left + right) // 2

    max_left_sum = divide_and_conquer(A,left,center) # 递归求左边最大子列和
    max_right_sum = divide_and_conquer(A,center+1,right) # 递归求右边最大子列和

    # 求跨越中线的最大子列和
    max_left_border_sum = left_border_sum = 0
    for i in range(center, left-1, -1):
        left_border_sum += A[i]
        max_left_border_sum = max(left_border_sum, max_left_border_sum)

    max_right_border_sum = right_border_sum = 0
    for i in range(center+1, right+1):
        right_border_sum += A[i]
        max_right_border_sum = max(right_border_sum, max_right_border_sum)

    # 比较1、2递归求出左边和右边的最大子列和。
    # 3、横跨中间的最大子列和。
    return max3(max_left_sum, max_right_sum, max_right_border_sum + max_left_border_sum)

def max_subseq_sum3(A):
    if not A: # 如果A列表是空的
        return 0
    return divide_and_conquer(A,0,len(A)-1)

# 测试
arr = [-2, 11, -4, 13, -5, -2]
print(f"分治法求最大子列和：{max_subseq_sum3(arr)}")