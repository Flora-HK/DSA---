# 1. 快排1.0版本
def quick_sort(arr: list[int]) -> list[int]:
    '''
    利用了类似于解决荷兰旗问题的思路
    递归式的引用当前数组的最后一个数作为基准值
    让当前的数组满足arr中的小于等于a的数放在数组的左边,大于a的数放在数组的右边标准
    每次排序都可以搞定一个数的位置,所以时间复杂度是O(N^2)
    '''
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    pivot_index = partition(arr, pivot) # 对数组进行排序并且返回基准值的索引
    left = quick_sort(arr[:pivot_index])
    right = quick_sort(arr[pivot_index + 1:]) # 此处的划分不包含pivot_index
    return left + [arr[pivot_index]] + right   # 注意这里需要将基准值放在中间,所以需要单独处理

def partition(arr: list[int], a: int) -> int:
    '''
    接收数组和基准值,在简单排序过程中,只对前len(arr) - 1个元素进行排序
    完成排序之后将基准数与小于区的下一个元素交换位置,并在最后返回小于区下标,便于后续继续递归划分数组进行处理
    '''
    left = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i]  <= a:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        else:
            i += 1
    arr[left], arr[-1] = arr[-1], arr[left]
    return left

if __name__ == '__main__':
    arr = [9, 8, 5, 6, 5, 4, 3, 5, 1]
    print(quick_sort(arr))


# 2. 快排2.0

def quick_sort2(arr: list[int], l: int, r: int):
    '''
    解决该问题使用了解决荷兰旗的思路,将数组划分为三部分，小于区，等于区，大于区
    每次排序取当前数组的最后一个数作为基准值，将小于基准值的数放在小于区，大于基准值的数放在大于区，等于基准值的数放在等于区
    递归式的对小于区和大于区进行以上操作，直到数组长度小于等于1
    时间复杂度O(N^2),基准值选的很偏产生差情况
    '''
    if l >= r:
        return
    p = partition2(arr, l, r)
    quick_sort2(arr, l, p[0] - 1)
    quick_sort2(arr, p[1] + 1, r)


def partition2(arr: list[int], l : int, r: int)  -> list[int]:
    '''解决方式：左右区各给一个指针，分别控制小于区和大于区'''
    left = l - 1
    right = r + 1
    i = l
    pivot = arr[r]
    while i < right:
        if arr[i] < pivot:
            left += 1
            arr[left], arr[i] = arr[i], arr[left]
            i += 1
        elif arr[i] > pivot:
            right -= 1
            arr[right], arr[i] = arr[i], arr[right]
        else:
            i += 1
    return [left + 1, right - 1] # 返回等于区的左右边界

if __name__ == '__main__':
    arr = [9, 8, 5, 6, 5, 4, 3, 5, 1]
    quick_sort2(arr, 0, len(arr) - 1)
    print(arr)

# 3. 快排3.0版本
# 在选择基准值pivot时，可以随机选择一个数，也可以选择中间的数，也可以选择第一个数
# 在这样的改进之下，时间复杂度是各种情况下时间复杂度求得的期望，时间复杂度变成了O(NlogN)，空间复杂度是O(logN)
import random
def quick_sort3(arr: list[int], l: int, r: int) -> None:
    if l > r:
        return
    pivot =  random.randint(l,  r) # 随机选择一个数,将其放在末尾，在调用partition2进行排序
    arr[r], arr[pivot] = arr[pivot], arr[r]
    p = partition2(arr, l, r)
    quick_sort3(arr, l, p[0] - 1)
    quick_sort3(arr, p[1] + 1, r)

if __name__ == '__main__':
    arr = [9, 8, 5, 6, 5, 4, 3, 5, 1]
    quick_sort3(arr, 0, len(arr) - 1)
    print(arr)


