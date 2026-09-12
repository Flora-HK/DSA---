
def heapify(arr: list[int], index: int, heapsize: int) -> None:
    '''
    下沉调整: 从index处开始调整大小为heapsize的堆arr:
    '''
    left: int = index * 2 + 1 # 左孩子节点
    while(left < heapsize): # 当左孩子节点存在时
        right: int = left + 1 # 右孩子节点
        largest: int = left
        if right < heapsize and arr[right] > arr[left]:
            largest = right # 右孩子节点存在且比左孩子节点大
        '''选出左右孩子节点中的较大的一个,将其下标传给largest'''
        if arr[index] > arr[largest]:
            break
        else:
            arr[index], arr[largest] = arr[largest], arr[index]
            index = largest # 更新“当前”位置下标
            left = index * 2 + 1 # 更新左孩子节点下标


def  heapinsert(arr: list[int], index: int) -> None:
    '''
    上浮调整 :从下往上的大根堆调整过程、从叶子节点index到顶部
    '''
    while(index > 0 and arr[index] > arr[(index - 1) // 2]):
        arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]
        index = (index - 1) // 2
    return

def heapsort(arr: list[int]) -> None:
    '''
    堆排序
    '''
    if len(arr) <= 1:
        return
    '''
    for i in range(len(arr)):
        heapinsert(arr, i)
        print(f'heapinsert: {arr}')
    '''
    for i in range(len(arr) - 1, -1, -1):
        '''
        对一开始的构建堆操作进行优化, 换成从叶子节点逐个执行heapify()操作，
        这样可以让该构建大根堆操作的时间复杂度变成O(N)
        '''
        print(f'[i]: {i}')
        heapify(arr, i, len(arr))
        print(f'heapify: {arr}')
    print(f'[arr] : {arr}')
    heapsize: int = len(arr) - 1
    arr[0], arr[heapsize] = arr[heapsize], arr[0]
    print(f'heapsize: {heapsize}, arr: {arr}')
    while(heapsize > 1):
        heapify(arr, 0, heapsize)
        heapsize -= 1
        arr[0], arr[heapsize] = arr[heapsize], arr[0]
        print(f'heapsize: {heapsize}, arr: {arr}')
    return 


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    heapsort(arr)
    print(arr)


# 存在某个堆，其元素有特点：在排好小根堆之后，任何元素的index跨度不会超过某个值k（k相对于整个数组来说是比较小的），请对符合该条件的堆进行排序

# 实现方法：每次选择前k + 1个数，将其输入到java的优先队列建立的小根堆里（此处使用java直接提供的小根堆是因为该算法只需要用到优先队列的有序弹入弹出功能），第一次排序就可以得出0位置上是最小的数，将该数弹出，放在 `result[]` 的0位置。然后再将第 k + 2 个数压入优先队列中，并将新小根堆的最小者弹出放在 `result[1]` 以此类推，直到 k + n 超出了范围，此时直接将排序用的小根堆元素依次弹出排列在 `result[]` 后即可

# 该方法时间复杂度： `O(N*logk)` ，每次对k个数进行堆排序，复杂度 `O(logk)` ，总共N个数，则为 `O(N*logk)`

import heapq # java的优先队列实现方法
def ksort(arr: list[int], k: int) -> list[int]:
    '''
    arr: 待排数组
    k: 对应特性参数
    '''
    min_heap = arr[ : k + 1]
    result = []
    heapq.heapify(min_heap)
    print(f'[heaplist]: {min_heap}')
    index = k + 1
    print(f'[index]:{index}')
    n = len(arr)
    for index in range(k + 1, n):
        heapq.heappush(min_heap, arr[index])
        result.append(heapq.heappop(min_heap))
        print(f'[result]: {result}, [min_heap]: {min_heap}, [index]:{index}')
    while(min_heap):
        result.append(heapq.heappop(min_heap))

    return result



if __name__ == '__main__':
    arr = [6, 5, 3, 2, 8, 10, 9]
    k = 3
    print(f'[ksort(arr, 3)] = {ksort(arr, k)}')




