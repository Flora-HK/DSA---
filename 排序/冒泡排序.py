
def popsort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def swap(x: int, y: int) -> tuple[int, int]:
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y


if __name__ == '__main__':
    arr = [5,4,3,2,1]
    print(popsort(arr))          