# 桶： 一种先入先出的队列容器
# 可以使用若干个桶进行桶排序

# 1. 基数排序： 桶排序的一种，按数字的每一位进行排序
def get_radix_rounds(arr: list[int], l: int, r: int) -> int:
    '''获取桶号'''
    if l >= r:
        return 0
    num = max(arr[l : r + 1])
    bucket_num = 0
    while(num):
        num //= 10
        bucket_num += 1
    return bucket_num

def get_digit(arr_num: int, num: int) -> int:
    '''获取对应位的数字'''
    '''
    while(num):
        r: int = arr_num % 10
        arr_num //= 10
        num -= 1
    return r
    '''
    return arr_num // (10 ** (num - 1)) % 10 # 优化后的取数方法，其中“10 ** (num - 1)”表示要取的位的权重
 

def radix_sort(arr: list[int], l: int = 0, r: int = -1, bucket_num: int = 10) -> list[int]:
    '''桶排序'''
    if l >= r:
        return
    radix = 10
    for i in range(1, bucket_num + 1):
        count: list[int] = [0] * radix
        bucket: list[int] = [0] * (r - l + 1)
        for j in range(l, r+1):
            x = get_digit(arr[j], i)
            count[x] += 1
        for j in range(1, radix):
            count[j] += count[j - 1]
        for j in range(r, l-1, -1):
            x = get_digit(arr[j], i)
            bucket[count[x] - 1] = arr[j]
            count[x] -= 1
        arr[l : r + 1] = bucket
    return arr

if __name__ == '__main__':
    arr = [123,312,79,5,78]
    print(bucket_sort(arr, 0, len(arr) - 1, get_radix_rounds(arr, 0, len(arr) - 1)))        






