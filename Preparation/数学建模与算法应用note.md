# 2

## 2-2 分别计算文件中每一行某个字符出现的次数

```
import numpy as np
a = []
with open('data2_2.txt') as f: # 打开文件
    for (i,s) in enumerate(f): # 用一个循环来查看所有的文件内容，变量i是行号（从0开始），变量s是行的内容（不包括末尾的换行符)。enmuerate是一个内置函数，它能并返回一个枚举对象。这个枚举对象生成一个包含两个元素的元组：一个是元素的索引，另一个是元素本身。例如，如果 a 是 [10, 20, 10]，那么 enumerate(a) 将生成 [(0, 10), (1, 20), (2, 10)]。
        a.append(s.count('a'),s.count('g'),s.count('c'),s.count('t'))
b=np.array(a)
print (b)
```

