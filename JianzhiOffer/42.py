# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 19:39:48
# LastEditTime: 2020-12-05 21:19:23
# LastEditors: ssdcxy
# Description: 连续子数组的最大和
# FilePath: /arithmetic_oj/JianzhiOffer/42.py

import json
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
        return max(nums)
        

def stringToIntegerList(input):
    return json.loads(input)

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
            
            ret = Solution().maxSubArray(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()