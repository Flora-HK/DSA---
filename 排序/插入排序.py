
def insertionSort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return  arr

if __name__ == '__main__':
    arr = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10]
    print(insertionSort(arr))