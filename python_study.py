'''
此题目整理自
https://www.cnblogs.com/tom-gao/p/6645859.html
https://blog.csdn.net/u013679490/article/details/54948759
'''

'''
1、什么是lambda函数？它有什么好处?

答：lambda 表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数

lambda函数：首要用途是指点短小的回调函数

lambda [arguments]:expression
'''
a = lambda x, y: x + y
print(a(3, 11))

'''
2、请写出一段Python代码实现删除一个list里面的重复元素
答：

1,使用set函数，set(list)

2，使用字典函数，
'''

a = [1, 2, 4, 3, 4, 5, 6, 4, 7, 8, 9, 0]
b = {}
b = b.fromkeys(a)
c = list(b.keys())
print(c)

'''
3、编程用sort进行排序，然后从最后一个元素开始判断

'''
a = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]
a.sort()
print(a)
last = a[-1]
print(last)
e = range(len(a) - 2, -1, -1)
print(e)
for i in range(len(a) - 2, -1, -1):
    # print(i)
    if last == a[i]:
        del a[i]
    else:
        last = a[i]
print(a)

'''
4、Python里面如何拷贝一个对象？（赋值，浅拷贝，深拷贝的区别）
答：赋值（=），就是创建了对象的一个新的引用，修改其中任意一个变量都会影响到另一个。

copy.copy()是浅拷贝：创建一个新的对象，但它包含的是对原始对象中包含项的引用（如果用引用的方式修改其中一个对象，另外一个也会修改改变）{1,完全切片方法；2，工厂函数，如list()；3，copy模块的copy()函数}

copy.deepcopy()是深拷贝：创建一个新的对象，并且递归的复制它所包含的对象（修改其中一个，另外一个不会改变）{copy模块的deep.deepcopy()函数}

'''
import copy

lista = [1, 2, 3, ['a', 'b']]
listb = copy.copy(lista)
listc = copy.deepcopy(lista)
print("-------- 初始化赋值 --------")
print(lista)  # [1, 2, 3, ['a', 'b']]
print(listb)  # [1, 2, 3, ['a', 'b']]
print(listc)  # [1, 2, 3, ['a', 'b']]
print("-------- 对lista加一个元素后 --------")
lista.append(5)
print(lista)  # [1, 2, 3, ['a', 'b'], 5]
print(listb)  # [1, 2, 3, ['a', 'b']]
print(listc)  # [1, 2, 3, ['a', 'b']]
print("-------- 对lista其中一个元素变动后 --------")
lista[3].append('c')
print(id(lista[2]))  # 1371472400
print(id(listb[2]))  # 1371472400
listb[2] = 6
print(id(lista[2]))  # 1371472400
print(id(listb[2]))  # 1371472496
print(id(lista[3]))  # 1208472828232
print(id(listb[3]))  # 1208472828232
print(id(listc[3]))  # 1208472828424
print(lista)  # [1, 2, 3, ['a', 'b', 'c'], 5]
print(listb)  # [1, 2, 6, ['a', 'b', 'c']]
print(listc)  # [1, 2, 3, ['a', 'b']]

'''
5、如何用Python来进行查询和替换一个文本字符串？

答：可以使用re模块中的sub()函数或者subn()函数来进行查询和替换，

格式：sub(replacement, string[,count=0])（replacement是被替换成的文本，string是需要被替换的文本，count是一个可选参数，指最大被替换的数量）

subn()方法执行的效果跟sub()一样，不过它会返回一个二维数组，包括替换后的新的字符串和总共替换的数量
'''
import re

p = re.compile('blue|white|red')
print(p.sub('color', 'blue socks and red shoes'))  # color socks and color shoes
print(p.sub('color', 'blue socks and red shoes', count=1))  # color socks and red shoes
print(p.sub('color', 'blue socks and red shoes', count=2))  # color socks and color shoes

print(p.subn('color', 'blue socks and red shoes'))  # ('color socks and color shoes', 2)
print(p.subn('color', 'blue socks and red shoes', count=1))  # ('color socks and red shoes', 1)
print(p.subn('color', 'blue socks and red shoes', count=2))  # ('color socks and color shoes', 2)

'''
6、Python里面match()和search()的区别？

答：re模块中match(pattern,string[,flags]),检查string的开头是否与pattern匹配。

re模块中research(pattern,string[,flags]),在string搜索pattern的第一个匹配值。
'''
print(re.match('super', 'superstition').span())  # (0, 5)
print(re.match('super', 'insuperable'))  # None

print(re.search('super', 'superstition').span())  # (0, 5)
print(re.search('super', 'insuperable').span())  # (2, 7)

'''
7、请在下面的空白处填写运行结果
'''
seq = [11, 12, 13, 14]
print("seq[:2]结果为：{0}".format(seq[:2]))  # [11, 12]
print("seq[-2:]结果为：{0}".format(seq[-2:]))  # [13, 14]
print("seq[10:]结果为：{0}".format(seq[10:]))  # []
print("seq[::-1]结果为：{0}".format(seq[::-1]))  # [14, 13, 12, 11]
print("seq[:]结果为：{0}".format(seq[:]))  # [11, 12, 13, 14]
# id() 函数用于获取对象的内存地址。
print(id(seq[:]))
print(id(seq))
print("id(seq[:]) == id(seq)结果为：{0}".format(id(seq[:]) == id(seq)))  # False

'''
8、优化以下程序
result = []
for x in range(10):
result.append(x ** 2)
print(result)
'''
# 优化后
result = [x ** 2 for x in range(10)]
print(result)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

'''
9、函数、类方法定义中如何实现可选参数、可选关键词参数
'''


def funcArgsTest(a, b, c=100, *args, **kwargs):
    sum = a + b + c
    for d in args:
        sum += d
    # for v in kwarg.itervalues():##values返回字典中的值，itervalues已经不被python3支持。##
    for v in kwargs.values():
        sum += v
    return sum


print(funcArgsTest(100, 200, 300, 500, 600, 00, 3, 45, 6, 4, 3, aa=700, bb=900, cc=1000, ac=11111))

'''
10、什么是装饰器，如何使用装饰器
'''


def log(level):
    def dec(func):
        def wrapper(*kargc, **kwargs):
            print("before func was called")
            func(*kargc, **kwargs)
            print("after func was called")

        return wrapper

    return dec


@log(2)
def funcLog():
    print("funcLog was called")


funcLog()
