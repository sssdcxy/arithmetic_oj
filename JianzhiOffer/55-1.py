# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 11:11:51
# LastEditTime: 2020-12-09 11:11:46
# LastEditors: ssdcxy
# Description: 二叉树的深度
# FilePath: /arithmetic_oj/JianzhiOffer/55-1.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left) + self.maxDepth(root.right)) 
        # if not root: return 0
        # queue = [root]
        # layer = 0
        # while queue:
        #     layer += 1
        #     n = len(queue)
        #     for _ in range(n):
        #         node = queue.pop(0)
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        # return layer

        

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
            
            ret = Solution().maxDepth(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()