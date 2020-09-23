# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/21 9:19  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import time
import matlab.engine
import matlab
import numpy as np
from utils import load_dataset

# time_1 = time.time()
# #可以为所欲为的调用matlab内置函数
print("启动matlab引擎中...")
eng = matlab.engine.start_matlab()
print("matlab引擎成功启动！")
# time_2 = time.time()
eng.addpath(eng.genpath("./alg_src_code/alg_matlab/"))

img_x, img_y, X, Y, ground_truth = load_dataset.load_mat("./data/demo_dataset/1001.mat")
result = eng.LPM(matlab.double(X.tolist()), matlab.double(Y.tolist()), nargout=1)
result = np.array(result).flatten().astype(int)
print(result)