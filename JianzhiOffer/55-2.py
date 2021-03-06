# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 13:41:04
# LastEditTime: 2020-12-09 11:21:38
# LastEditors: ssdcxy
# Description: 平衡二叉树
# FilePath: /arithmetic_oj/JianzhiOffer/55-2.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recursive(cur):
            if not cur: return 0
            left = recursive(cur.left)
            if left == -1: return -1
            right = recursive(cur.right)
            if right == -1: return - 1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return recursive(root) != -1

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

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
            root = stringToTreeNode(line);
            
            ret = Solution().isBalanced(root)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()