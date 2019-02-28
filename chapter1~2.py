
第二章
In [2]:
import numpy as np
data = {i:np.random.randn() for i in range(7)}
data
Out[2]:
{0: -0.507227357774868,
 1: -0.5473118275710105,
 2: 0.10624791755388938,
 3: 0.6205686364305621,
 4: -0.5602910918629387,
 5: -0.4147882858341796,
 6: -0.7997456407591227}
自省

In [6]:
b = [1,2,3]
In [12]:
b?
In [13]:
print?
In [14]:
#这可以作为对象的自省，如果对象是一个函数或实例方法，定义过的文档字符串，也会显示出信息；
In [15]:
def add_number(a,b):
    """
    Add two numbers together
    Return
    the_sum:type of arguments
    """
    return a+b
In [16]:
add_number? #显示文档字符串
In [17]:
add_number??#会显示函数的源码
In [18]:
#  ？还有一个用途，就是想Unix或windows命令一样搜索Ipython的命名空间。字符与通配符结合可以匹配所有的名字，
#例如可以获取所有包含load的顶级numpy命名空间
In [22]:
np.*load*?
In [23]:
# np.__loader__
# np.load
# np.loads
# np.loadtxt
# np.pkgload
In [24]:
# %run 命令
In [25]:
#可以用%run 命令运行所有的python程序
In [26]:
#在 jupyter notebok 中，可以使用%load 将脚本导入到一个代码格中：
# %load ipython_script_test.py
In [27]:
# 魔术命令
#魔术命令在指令前添加百分号%前缀。
#例如：可以使用%timeit测量任何python语句，例如矩阵乘法的执行时间
In [28]:
a = np.random.randn(100,100)
In [29]:
%timeit np.dot(a,a)
60.1 µs ± 629 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
In [30]:
#魔术命令有命令行选项，可以通过？查看
In [31]:
%debug?
In [32]:
#魔术命令默认可以不用百分号，只要没有变量与函数名相同，被称为自动魔术命令，可以用%automagic打开或关闭
In [33]:
#一些魔术命令与python函数很像，它的结果可以赋值给一个变量
In [36]:
%pwd
Out[36]:
'/Users/Camus/Desktop/MySelf/python_note/python_for_data'
In [39]:
foo = %pwd
foo
Out[39]:
'/Users/Camus/Desktop/MySelf/python_note/python_for_data'
In [40]:
%matplotlib inline
In [42]:
import matplotlib.pyplot as plt
plt.plot(np.random.randn(50).cumsum())
Out[42]:
[<matplotlib.lines.Line2D at 0x10d93e208>]

In [ ]:
#变量和参数传递
In [43]:
#当在python中创建变量（或名字），就在等号右边创建了一个对这个变量的引用。
In [44]:
a = [1,2,3]
#假设将a赋值给一个新变量b
b=a
In [45]:
#在python中，a和b实际上是同一个对象，即原有列表[1,2,3]
In [46]:
#在a中添加一个元素
a.append(4)
In [47]:
b
Out[47]:
[1, 2, 3, 4]
In [48]:
#可以用isinstance函数检查对象是某个类型的实例：
a = 5
isinstance(a,int)
Out[48]:
True
In [49]:
#可变对象
#例如：列表、字典、Numpy数组和用户自定义的类，即这些对象或包含的值可以被修改
In [50]:
#不可变对象
#例如字符串和元组，是不可变的；
In [51]:
#数值类型
#python的主要数值类型是int和float。int可以存储任意大的数
#浮点数使用python的float类型。
In [52]:
#字符串
#可以用单引号或者双引号来写字符串
#对于有换行符的字符串，可以使用三引号“”“，”“”
In [56]:
c ="""
this is a dog
cat
"""
#字符串c可以用count方法计算c中的新的行：
In [57]:
c.count('\n')
Out[57]:
3
In [59]:
#python对象可以使用str函数转化为字符串：
a = 5.6
s = str(a)
s
Out[59]:
'5.6'
In [62]:
#字符串是一个序列的Unicode字符，因此可以像其他序列，比如元组和列表一样处理：
s = 'python'
list(s)
Out[62]:
['p', 'y', 't', 'h', 'o', 'n']
In [63]:
s[0:3]
Out[63]:
'pyt'
In [66]:
#反斜杠是转移字符，意思是它被用来表示特殊字符
#要写一个包含反斜杠的字符串，需要进行转义：
s = '12\\34'
s
Out[66]:
'12\\34'
In [68]:
#如果字符串中包含许多反斜杠，但没有特殊字符，这样做就很麻烦，可以在字符串前面加r，表明字符就是它自身：
s = r'this\hsa\no\special\characters'
s
Out[68]:
'this\\hsa\\no\\special\\characters'
In [69]:
#将两个字符串合并，会产生一个新的字符串
a = 'abc'
b = 'def'
a+b
Out[69]:
'abcdef'
In [70]:
#字符串的模版化或格式化，字符串有format方法，可以替换格式化的参数为字符串，产生一个新的字符串
In [71]:
#比较运算符
In [96]:
#要判断两个引用是否指向同一个对象，可以使用is方法，is not可以判断两个对象是不同的
a = [1,2,3]
b = a
c = list(a)
print(c)
[1, 2, 3]
In [97]:
a is not c
Out[97]:
True
In [98]:
print(c)
[1, 2, 3]
In [99]:
a == c
Out[99]:
True
In [100]:
a == b
Out[100]:
True