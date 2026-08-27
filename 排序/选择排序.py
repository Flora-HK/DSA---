
def SelectSort(arr: list):
    '''每次从i到n-1中找到最小值，放到开头， 时间复杂度为O(n^2)'''
    if len(arr) < 2 or arr is None:
        return arr
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            min_index = j if arr[j] < arr[min_index] else min_index
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == '__main__':
    arr = [5,4,3,2,1]
    print(SelectSort(arr))
