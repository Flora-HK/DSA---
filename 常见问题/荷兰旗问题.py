# 给出一个数a，一个数组arr，请将arr中的小于等于a的数放在数组的左边，大于a的数放在数组的右边

def partition(arr: list[int], a: int) -> None:
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