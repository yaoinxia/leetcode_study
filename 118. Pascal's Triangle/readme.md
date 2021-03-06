Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

给定非负整数numRows，生成Pascal三角形的第一个numRows。


在Pascal的三角形中，每个数字是它上面两个数字的总和。

**Example:**

Input: 5
Output:
~~~
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
~~~
**思路：**

- 每一层都是一个列表存储，层数等于列表长度，后一层的元素数与其前一层中的元素是相关的。
- 二维列表，定义大列表为l，l[][],其中
~~~
l[0]==[1]。l[0][0]==1。
l[1]==[1,1]。l[1][0]==1;l[1][1]==1;
l[2]==[1,2,1];l[2][0]=1;l[2][1]==2=l[1][0]+l[1][1];
~~~

~~~
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        l = [[1]]
        for i in range(1,numRows):
            print("==================================")
            print(i)
            l.append([])
            for j in range(i+1):
                print("++++++++++++++++++++++++")
                print(j)
                l[i].append((l[i - 1][j - 1] if j > 0 else 0) + (l[i - 1][j] if j < i else 0))
        return l

if __name__ == "__main__":
    print(Solution().generate(5))
~~~

**网上思路：**
<https://blog.csdn.net/coder_orz/article/details/51589254>