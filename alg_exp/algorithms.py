import matlab.engine
import matlab
import numpy as np


class Algorithm:
    def cal_feature_matching_result(self):
        pass

# the Method LPM
class LPM:
    def __init__(self, eng, X, Y):
        self.eng = eng
        self.X = X
        self.Y = Y

    def cal_feature_matching_result(self):
        result = self.eng.LPM(matlab.double(self.X.tolist()), matlab.double(self.Y.tolist()), nargout=1)
        result = np.array(result).flatten().astype(int)
        return result

# the Method RANSAC
class RANSAC:
    def __init__(self, eng, X, Y):
        self.eng = eng
        self.X = X
        self.Y = Y

    def cal_feature_matching_result(self):
        result = self.eng.RANSAC_alteration(matlab.double(self.X.T.tolist()), matlab.double(self.Y.T.tolist()), nargout=1)
        result = np.array(result).flatten().astype(int)
        return result

# 现在有两种方法:LPM、RANSAC
class Algorithm_Cal:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        # 启动matlab引擎
        print("matlab引擎启动中...")
        self.eng = matlab.engine.start_matlab()
        self.eng.addpath(self.eng.genpath("../alg_src_code/alg_matlab/"))
        print("matlab引擎已经启动...")
        self.alg_map = {'LPM': LPM(self.eng, self.X, self.Y), 'RANSAC': RANSAC(self.eng, self.X, self.Y)}

    # 目前有的type为'LPM', 'RANSAC'
    # The current types are 'LPM' and 'RANSAC'.
    def cal_feature_matching_result(self, type):
        return self.alg_map[type].cal_feature_matching_result()


if __name__ == '__main__':
    from utils import load_dataset
    img_x, img_y, X, Y, ground_truth = load_dataset.load_mat("../data/demo_dataset/1001.mat")
    algorithm_cal = Algorithm_Cal(X, Y)
    result = algorithm_cal.cal_feature_matching_result('LPM')
    result = algorithm_cal.cal_feature_matching_result('RANSAC')

