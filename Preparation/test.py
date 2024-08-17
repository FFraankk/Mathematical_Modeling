import numpy as np
import string
import random
import pandas as pd
# a = []
# with open('data2_2.txt') as f:
#     for (i,s) in enumerate(f):
#         a.append([s.count('a'),s.count('g'),s.count('c'),s.count('t')])
# b=np.array(a)
# print (b)


# from numpy.random import randint
# import numpy as np

# a = randint(10,20,16)
# ma =max(a)
# ind1 = [index for index,value in enumerate(a) if value==ma ] 
# ind2 = np.where(a == ma)
# print(ind1)
# print(ind2[0])


# x = string.ascii_letters + string.digits # x是所有数字和字母的一个东西
# y = ''.join([random.choice(x) for i  in range(1000) ]) #在一个空的字符串后面加上随机取1000个字符，相当于直接生成了1000个字符；choice（）从多个元素中选择一个
# d = dict()
# for ch in y:
#     d[ch] = d.get(ch,0)+1 #  尝试从字典d中获取字符ch的当前计数并且+1，如果字符ch不存在于字典中，则返回默认值0
# for k,v in sorted(d.items()):
#     print(k,'-',v)

# a1 = np.array([1,2,3,4])
# a2 = a1.astype(float)
# print(a1.dtype)
# print(a2.dtype)

# dates= pd.date_range(start='20191101',end='20191124',freq='D')
# a1 = pd.DataFrame(np.random.randn(24,4),index=dates,columns=list('ABCD'))
# a2 = pd.DataFrame(np.random.rand(24,4))

with open('data.txt') as fp:
    L1 = [ ]
    L2 = [ ]
    for line in fp:
        L1.append(len(line))
        L2.append(len(line.strip()))
data = [str(num)+'\t'for num in L2]
