#1. 查找某组有序数据中的指定数字num

def find_num(nums: list[int], num: int) -> int:
    right = len(nums) - 1
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == num:
            return nums[mid]
        elif nums[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8]
    num = 9
    print(f'nums = {nums}, num = {num}')
    print(f'[find_num]: {find_num(nums, num)}')


#2. 查找某个有序数组中，大于等于num的最左侧的位置、小于等于num的最右侧的位置

def find_num2(nums: list[int], num: int) -> int:
    res = 0
    right = len(nums) - 1
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= num:
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res

if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
    num = 3
    print(f'nums = {nums},  num = {num}')
    print(f'[find_num2]: {find_num2(nums, num)}')


#3. 在某个无序的数组arr中(相邻两个数必不相等)，给出一个定义——局部最小值：左右两边都不大于自己的值，求arr中的局部最小值（要求时间复杂度在O(N)）

def is_min(nums, index):
    '''检查index位置的数是否是局部最小值'''
    if index == 0:
        return nums[index] < nums[index + 1]
    elif index == len(nums) - 1:
        return nums[index] < nums[index - 1]
    else:
        return nums[index] < nums[index - 1] and nums[index] < nums[index + 1]


def find_min(nums: list[int]):
    '''使用二分法进行查找该无序数组中的局部最小值，先看mid是不是局部最小值，如果不是，则看mid的左边或右边是不是局部最小值，直到找到为止'''
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if is_min(nums, mid):
            return mid
        elif nums[mid] > nums[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == '__main__':
    nums = [2, 1, 3, 4, 6, 5, 8, 7, 9]
    print(f'nums = {nums}')
    print(f'[find_min]: {find_min(nums)}')


# 4. 二分法的mid值计算，使用left + (right - left) / 2 = left + (right - left) >> 1可以保证无溢出情况发生，
# (left + right) / 2，可能会出现left+ right溢出的情况发生，这样会导致mid为负值


def find_max(arr: list[int], left: int, right: int) -> int:
    '''用二分递归的方法来查找某个数组的最大值'''
    if left == right:
        return arr[left]
    mid = left + ((right - left) >> 1)
    left_max = find_max(arr, left, mid)
    right_max = find_max(arr, mid + 1, right)
    return max(left_max, right_max)

if __name__ == '__main__':
    nums = [2, 1, 3, 4, 6, 5, 8, 7, 9]
    print(f'nums = {nums}')
    print(f'[find_max]: {find_max(nums, 0, len(nums) - 1)}')
