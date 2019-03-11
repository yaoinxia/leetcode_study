#!/usr/bin/env python
# _*_ coding:utf-8 _*_

第二题题目：求最长重复子串。假设字符串S和子串S1满足S.charAt(i) == S1.charAt(i%S1.length()); 则子串S1是S的一个重复子串。求满足条件最长子串。

比如 "abcabcabc" 的最长重复子串就是"abc"

解题思路：暴力破解法，时间复杂度n平方。

具体过程：子串的长度从n/2开始测试，遍历整个字符串，如果符合重复子串的要求车返回当前子串，否则子串长度减1.如果子串长度最后是0，则返回整个字符串。

具体代码很简单：

    public void compute(String s){
        int res = 0;
        for(int i = 1 ;i < s.length();i++){
           boolean find = true;
           res = i;
           for(int j = 1; j < s.length() ; j++){
              if(s.charAt(j%i) == s.charAt(j))
                  continue;
              else{
                  find = false;
                  break;
              }
           }
           if(find == true)
              break;
        }
        System.out.print(s.substring(0,res));
    }
 
第三题
二维生物的旅行

二维生物hip当前处于x轴的0坐标位置，打算去拜访它的老友hop，hop位于坐标轴的target位置。hip有一个很奇怪的能力，其迈出的第n步（从1算起），步长为n。也就是说第一步可以移动的距离为1，第二步可以移动的距离为2，以此类推。每走一步之前，hip都可以决定这一步是向左走还是向右走，但每一步都只能朝一个方向前进。二维生物都很懒，hip希望你能先帮他计算出最少需要走多少步才能到达target位置，他再决定要不要去拜访老友。

输入描述：

每个测试输入包含1个测试用例，即给出目标位置target的值。这里保证 - 10 ^ 9 <= target <= 10 ^ 9, 且为整数

public
static
int
compute(int
target){
    int
n = Math.abs(target);
int
k = (int)
Math.ceil((Math.sqrt(8 * n + 1) - 1) / 2);
int
total = k * (k + 1) / 2;
int
d = total - n;
if (d % 2 == 0)
return k;
else if (d + k + 1 % 2 == 0)
    return k + 1;
else
    return k + 2;
}
第四题
靓号问题

描述：手机号码0 - 9，一个手机号码至少有K位数相同则为靓号，若修改号码中的一个数字需要的金额为新数字与旧数字的差值（绝对值），问给出一个号码，改成靓号需要多少钱。

解题思路：

1）对于给定的k, 分别求得相同个数满足看，数字为0 - 9
分别所需要的花费，最小的就是答案。

2）对于变换成指定数字，有很多种方法，哪一种最小呢？就是先从当前数字最近的开始找，比如
13245
变换成至少3个1，那么先找离数字1最近的，距离为1或者 - 1
的数字2，此时k还不满足要求，在找距离为2的数字3，此时满足幸运数字定义。得到花费c。

3）对于2），很明显那是花费最小的搜索路径。

最后一题代码参考：

https: // blog.csdn.net / wuyifan1115 / article / details / 81163285

代码如下：

public
static
void
test4()
{
Scanner
scanner = new
Scanner(System. in);
int
N = scanner.nextInt();
int
K = scanner.nextInt();
String
s = scanner.next();
StringBuffer
ans = null;
int
res = (int)
1e9;
for (int i=0;i < 10;i++){
StringBuffer t=new StringBuffer(s);
int p=K, c=0;
for (int j=0;j < 10;j++){
for (int l=0;l < N;l++){
if (p != 0 & & t.charAt(l)-'0' == i+j){
p--;
t.setCharAt(l, (char)(i+'0'));
c=c+j;
}
}
if (j != 0)
for (int l=N-1;l >= 0;l--)
if (p != 0 & & t.charAt(l)-'0' == i-j){
p--;
t.setCharAt(l, (char)(i+'0'));
c=c+j;
}
}
if (c < res){
res=c;
ans=t;
}

}
System.out.println(res);
System.out.println(ans);
}
