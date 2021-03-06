# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 12:05:03
# LastEditTime: 2020-11-26 20:19:33
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/JianzhiOffer/22.py

import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return None
        p1 = p2 = head
        while k:
            if p1.next:
                p1 = p1.next
                k -= 1
            else:
                return None
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2
        

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

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
            head = stringToListNode(line);
            line = next(lines)
            k = int(line);
            
            ret = Solution().getKthFromEnd(head, k)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()