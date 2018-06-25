# -*- coding: utf-8 -*-
#  @Time        :    2018/6/22 3:28
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    BinaryTreeMirror.py
#  @Place       :    dormitory
'''
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
思路：递归。可利用python特性简化代码。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


class BestSolution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            root.left, root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)


def main():
    pass


if __name__ == '__main__':
    main()
