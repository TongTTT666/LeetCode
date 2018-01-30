# Two Sum #
Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the same element twice.

**Example:**
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
---
## 关于python中 **字典(dict)** 部分的学习 ##
字典在本题中是用来创建对应关系的，相比于暴力搜索，利用字典记录先前信息可以大量减少程序运行的时间。首先，字典最关键的部分是其具备的三个要素：
- 键(key)：也即属性，例如“姓名”，“颜色”，“性别”等等
- 值(value)：也即属性对应的某个取值，例如“张三”，“黄色”，“男”等等。
- 变量名称：也即字典的名字，比如在本题中的变量名称便是“dict_need”。

根据三个要素各部分的功能，再结合本题的要求，很自然的想到如下思路：

本题是从数组中找到两个数加起来等于target，那么对应于一个已知的数，我们是一定能够求出它所需要的另外一个数的，因此存储这些信息一定是能够节省程序运行时间的（以空间换时间）。因此，我们需要构建以`需要数字：对应下标`为key:value单元的字典！也即key是需要的数字，那么是哪个数需要的这个数字呢？那就是value对应下标的那个数。通过遍历输入数组，这种信息会不断地保存在字典中。当遍历的数在字典中恰好发现了某个key是其需要的数，则程序结束，返回该数和key对应的value；反之，如果在字典中没有发现其需要的数，则把这个数的信息以`需要数字：对应下标`的方式加入字典当中即可。

**Example:**
例如给定`nums = [2, 7, 11, 15], target = 9`，当遍历到第一个数2的时候，很自然的构建如下字典信息：
<center>

`
target-2: 0
`
</center>
也即对应2所需要的数(7)和其所对应的下标。当遍历到第二个数7的时候，则发现7刚好是字典中的某个key值，所以返回7所对应的value和7所对应的下标即可。