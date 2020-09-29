# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/29 15:00  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
from alg_exp import algorithms
class Feature_Matching_Quan_Exp:
    # dataset是一个numpy.array，其中每一个维度就是一个数据
    # dataset is as numpy.array, where each dimension is a data
    # method_list方法列表，要求与alg_exp.algorithms中拥有的方法名称对应
    # method_list is required to correspond to the method names owned in alg_exp.algorithms.
    def __init__(self, dataset, method_list):
        self.dataset = dataset
        self.method_list = method_list

    # 主方法，要进行实验得依靠此方法
    # main method，when doing experiment mainly relies on this method。
    # 保存在excel中，方便展示，保存在mat中，方便后续的数据处理
    # saving in excel to show result easily， saving in mat to process data easily
    def start_exp(self, save_path_excel:str, save_path_mat:str, save_excel=True, save_mat=True):
        for data in self.dataset:
            X = 1
            Y = 1
            # 注入数据
            # inputting data
            algorithm_cal = algorithms.Algorithm_Cal(X, Y)
            for method in self.method_list:
                # 计算不同方法给出正确匹配
                # computing true matches given by each algorithm
                result = algorithm_cal.cal_feature_matching_result(method)
        return

    # 数据保存excel
    # saving data into excel
    def save_exp_result_2_excel(self, save_path):
        pass

    # 数据保存mats
    # saving data into mats
    def save_exp_result_2_mat(self, save_path):
        pass

# demo
# 样例
if __name__ == '__main__':
    pass



