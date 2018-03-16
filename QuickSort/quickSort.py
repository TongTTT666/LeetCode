import random


def Sort(array):
    # 返回情况
    if len(array) <= 1:
        return array

    # 分割，将array分割成两个部分
    # p1是比array[index]小的，p2是比array[index]大的
    # 随机挑选一个位置的数
    index = random.randint(0, len(array)-1)
    print(array[index])
    p1, p2 = [], []
    # 大的放一边，小的放一边
    for i in range(len(array)):
        if array[i] < array[index]:
            p1.append(array[i])
        else: 
            p2.append(array[i])
    
    # 放完继续排呗！
    Sorted_p1 = Sort(p1)
    Sorted_p2 = Sort(p2)
    
    # 返回两个相加即可，小的加大的！
    return Sorted_p1 + Sorted_p2
    



a = [2, 9, 5, 4, 1, 6]
b = [1, 2, 3]
#a.append(b[1])
#print(a)
print(Sort(a))
