'''
  第一次使用在git中创建新文件test1.py
'''
import numpy as np
import pandas as pd

data = np.linspace(0,9,10)
mydata = pd.DataFrame(data, columns=['number'], index=list('abcdefghij'))

print(mydata)
print("kylin")
