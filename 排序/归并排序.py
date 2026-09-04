
def merge_sort(arr: list[int]) -> list[int]:
    '''归并排序：
    将数组分成左右两部分，分别排序然后合并
    '''
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    '''排序合并左右两个数组'''
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

if __name__ == '__main__':
    arr = [1, 5, 3, 2, 4, 6]
    print(merge_sort(arr))