
def heapify(arr: list[int], index: int, heapsize: int) -> None:
    '''
    从index处开始调整大小为heapsize的堆arr:
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
    从下往上的大根堆调整过程、从叶子节点index到顶部
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
    for i in range(len(arr)):
        heapinsert(arr, i)
        print(f'heapinsert: {arr}')
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

