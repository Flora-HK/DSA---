
# 1. 有一组数据，其中一个数字出现了奇数次，其余数字均出现了偶数次，请找出这个出现了奇数次的数字
def find_num(arr: list[int]) -> int:
    '''对所有的数据一起进行异或运算，最后留下来的结果就是那个出现了奇数次的数字'''
    res = 0
    for num in arr:
        res ^= num
    return res


# 2. 有一组数据，其中有两个数字出现了奇数次，其余数字均出现了偶数次，请找出这两个出现了奇数次的数字
def find_nums(arr: list[int]) -> list[int]:
    '''先对所有的数据进行异或操作, 会得到x = a ^ b, 由于x != 0, 所以x为 1 的那一位， 肯定有a和b在该位上肯定一个为 1 , 一个为0.
      所以可以通过找到 a ^ b 的一个为 1 的位, 将arr中的数据分成两组: 一组是这一位为1的数据, 另一组是这一位为0的数据,  这样
      a = 所有这一位为1的数据异或的结果, b = 所有这一位为0的数据异或的结果'''
    x = 0
    for num in arr:
        x ^= num
    right_one = x & (~x + 1)  # 获取x最右边的1
    only_one = 0
    for num in arr:
        if num & right_one == 0:
            only_one ^= num

    return [only_one, x ^ only_one]


if __name__ == '__main__':
    print(f'[find_num]: {find_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])}')
    print(f'[find_nums]: {find_nums([1, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11])}')