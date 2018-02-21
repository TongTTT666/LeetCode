# MergeSort是最基本的快速排序方法，这是必须掌握的
# MergeSort的两步，一步是Sort另外一步是Merge


def Sort(array):
    # 返回情况
    if len(array) <= 1:
        return array

    # 分割，将array分割成两个部分
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # 经典三步骤
    sorted_left = Sort(left)
    sorted_right = Sort(right)
    return Merge(sorted_left, sorted_right)


def Merge(left, right):
    # 确定指针
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        print(left, right)
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    if i < len(left):
        res += left[i:]
    elif j < len(right):
        res += right[j:]

    return res


a = [2, 9, 5, 4, 1, 6]
b = [1, 2, 3]
#a.append(b[1])
#print(a)
print(Sort(a))