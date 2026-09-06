# 给出一个数a，一个数组arr，请将arr中的小于等于a的数放在数组的左边，大于a的数放在数组的右边

def partition(arr: list[int], a: int) -> list[int]:
    left = 0
    i = 0
    while i < len(arr):
        if arr[i]  <= a:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        else:
            i += 1
    return arr

if __name__ == '__main__':
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    a = 5
    print(partition(arr, a))

# 荷兰国旗问题：
# 给定一个数组arr，一个数num，请将小于num的数放在数组的左边，等于num的数放在数组的中间，大于num的数放在数组的右边

def partition2(arr: list[int], num: int)  -> list[int]:
    '''解决方式：左右区各给一个指针，分别控制小于区和大于区'''
    left = 0
    right = len(arr) - 1
    i = 0
    while i <= right:
        if arr[i] < num:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        elif arr[i] > num:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
        else:
            i += 1
    return arr

if __name__ == '__main__':
    arr = [10, 9, 5, 7, 6, 5, 4, 3, 2, 5]
    num = 5
    print(partition2(arr, num))
