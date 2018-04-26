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

注：
不会写

网上：https://blog.csdn.net/coder_orz/article/details/51506414
思路一:比较直观的思路，对于输入的n，我们可以跨 i=1, 2, 3, …, n/2 个两步台阶。对于这 n/2 种情况，每种情况需要跨 n-i 次，所以每种情况又有 C(n-i, i) 种不同的跨法。计算比较复杂。
思路二:当输入为1, 2, 3, 4, 5, 6, 7, 8, 9, 10时，观察输出为1, 2, 3, 5, 8, 13, 21, 34, 55, 89，是斐波那契数列！好了，我们找到了规律，写代码吧
思路三:找规律是一方面，另一方面我们要探究规律里隐藏的逻辑。当有n个台阶时，可供选择的走法可以分两类：1，先跨一阶再跨完剩下n-1阶；2，先跨2阶再跨完剩下n-2阶。所以n阶的不同走法的数目是n-1阶和n-2阶的走法数的和。 
这个时候如果用递归，复杂度会太大而无法AC，所以用动态规划记录历史数据，即可。





