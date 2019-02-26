'''
  第一次使用在git中创建新文件test1.py
'''
import numpy as np
import pandas as pd

data = np.arange(10)
mydata = pd.DataFrame(data, columns=['number'], index=list('abcdefghij'))

print(mydata)
