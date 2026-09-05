# 由mergesort排序方法改写可以实现的常见问题



# 1. 小和问题
#  对一个整形数组，其中的某个元素a[i]而言，它左侧小于它的元素之和为该元素的“小和”
# 某个数组的“小和”，是指该数组中所有元素的小和之和

def fun1():
    """
    暴力法(时间复杂度O(N^2))
    """
    pass

def Small_sum(arr:  list[int]) -> int:
    '''
    归并排序的过程可以顺便求出小和
    在merge的过程中，要使用左右两部分的指针进行对比，如果左侧部分的某个元素a < 右侧部分的某个元素b，
    则可知b右侧的剩下的元素都会比元素a大，则可有下标计算得出(len(右侧) - j) * a 的小和
    由于merge过程一直在排序，所以会简化比较的次数、同时使左侧部分的内部在merge过程已经完成了小和计算，所以不会重复计算
    时间复杂度O(NlogN)
    '''
    if len(arr) <= 1:
        return 0
    return process(arr, 0, len(arr) - 1)
    

def process(arr: list[int], l: int, r: int) -> int:
    if l == r:
        return 0
    mid = l + (r - l) // 2
    return process(arr, l ,mid) + process(arr, mid + 1, r) + merge(arr, l,  mid, r)


def merge(arr: list[int], l: int, mid: int, r: int) -> int:
    '''
    注意：当左组的数 == 右组的数的时候，需要先拷贝右组的数，再拷贝左组的数，否则会重复计算小和
    '''
    help = []
    p1 = l
    p2 = mid + 1
    res = 0
    while p1 <= mid and p2 <= r:
        res += (r - p2 + 1) * arr[p1] if arr[p1] < arr[p2] else 0
        if arr[p1] < arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1
    while p1 <= mid:
        help.append(arr[p1])
        p1 += 1
    while p2 <= r:
        help.append(arr[p2])
        p2 += 1
    for i in range(len(help)):
        arr[l + i] = help[i]
    return res

if __name__ == '__main__':
    arr = [1, 3, 4, 2, 5]
    print(Small_sum(arr))

# 2. 逆序对问题
# “逆序对”： 如果在一个数组中，左侧的数字a比右侧的数字b大，这两个数（a，b）构成一个逆序对，请求出某个数组的逆序对数量
# 本质上与小和问题实现过程对等，使用merge过程实现（小和问题：求解左侧有多少个数比当前的数小；逆序对问题：求解右侧有多少个数比当前的数小）

def inversion(arr: list[arr]) -> int:
    if len(arr) < 2:
        return 0
    return process2(arr, 0, len(arr) - 1)

def process2(arr: list[int], l: int, r: int) -> int:
    if l == r:
        return 0
    mid = l + (r - l) // 2
    return process2(arr, l, mid) + process2(arr, mid + 1, r) + merge2(arr, l, mid, r)

def merge2(arr: list[int], l: int, mid: int, r: int) -> int:
    help = []
    p1 = l
    p2 = mid + 1
    res = 0
    while p1 <= mid and p2 <= r:
        res += (mid - p1 + 1) if arr[p1] > arr[p2] else 0
        if arr[p1] < arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1
    while p1 <= mid:
        help.append(arr[p1])
        p1 += 1
    while p2 <= r:
        help.append(arr[p2])
        p2 += 1
    for i in range(len(help)):
        arr[l + 1] = help[i]
    return res

if __name__ == '__main__':
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(inversion(arr))   
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(inversion(arr))