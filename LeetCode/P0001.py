# -*- coding: utf-8 -*-
# @time       : 2019-10-13 22:01
# @author     : ssdcxy
# @email      : 18379190862@163.com
# @file       : P0001.py
# @description: 两数之和

from typing import List
import json


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            if num in nums_dict:
                return [nums_dict[num], i]
            else:
                nums_dict[target - num] = i


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            target = int(line);

            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()