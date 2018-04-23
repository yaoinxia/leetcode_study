You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

你正在爬楼梯的情况。 需要n个步骤才能到达顶端。

每次你可以爬1或2步。 有多少种不同的方式可以爬到顶端？

注意：给定n将是一个正整数。

例1：

输入：2
输出：2
说明：有两种方法可以爬到顶部。
1. 1步+ 1步
2. 2个步骤
例2：

输入：3
输出：3
说明：有三种方法可以爬到顶部。
1. 1步+ 1步+ 1步
2. 1步+ 2步
3. 2步+ 1步

初步想法：
方法总数：sum
类似树的结构，根节点定义为1或者2
每次从根节点开始遍历，依次减去每个节点的值，然后直到最后，减至为0




