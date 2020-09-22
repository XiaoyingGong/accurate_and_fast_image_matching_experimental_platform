# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/21 9:19  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：

# 基类 base class，
# 为了便于后续的维护，比如增加评价标准，在此使用了策略模式
# To facilitate subsequent maintenance, such as adding evaluation criteria. The Strategy pattern is used in this file.
#To facilitate subsequent maintenance, such as adding evaluation criteria
class Criterion:
    def cal(self):
        pass

# 有些特殊的情况会造成以下的值的分母为0，代码未对这些情况进行任何处理，
# 当发生时将会忽略，且将值保存为默认的-1(用户需要对这种情况进行相应处理)
# Some special cases would cause the denominator is 0, and the code does not handle these cases,\
# just save the reuslts as the default of -1.

# type = 'precision'
class Precision(Criterion):
    def __init__(self, TP, FP):
        self.TP = TP
        self.FP = FP
    def cal(self)->float:
        try:
            precision = self.TP / (self.TP + self.FP)
        except Exception:
            precision = -1
        return precision

# type = 'recall'
class Recall(Criterion):
    def __init__(self, TP, FN):
        self.TP = TP
        self.FN = FN
    def cal(self)->float:
        try:
            recall = self.TP / (self.TP + self.FN)
        except Exception:
            recall = -1
        return recall

# type = 'f1'
class F1(Criterion):
    def __init__(self, TP, TN, FP, FN):
        self.TP = TP
        self.TN = TN
        self.FN = FN
        self.FP = FP

    def cal(self)->float:
        p = Precision(self.TP, self.FP)
        precision = p.cal()
        r = Recall(self.TP, self.FN)
        recall = r.cal()
        try:
            f1 = 2 * (precision * recall) / (precision + recall)
        except Exception:
            f1 = -1
        return f1

# type = 'accuracy'
class Accuracy(Criterion):
    def __init__(self, TP, TN, FP, FN):
        self.TP = TP
        self.TN = TN
        self.FN = FN
        self.FP = FP

    def cal(self)->float:
        accuracy = (self.TN + self.TP) / (self.TP + self.TN + self.FP + self.FN)
        return accuracy

# 管理具体计算哪一种标准
# Used to choose using which criterion
class Cal_criterion():
    def __init__(self, TP, FP, FN, TN):
        # 可以更改写一个注册的功能，从配置文件来读
        self.criteria_map = {'precision': Precision(TP, FP),  'recall': Recall(TP, FN), 'f1': F1(TP, TN, FP, FN), \
                    'accuracy': Accuracy(TP, TN, FP, FN)}
    #
    def cal(self, type:str)->float:
        return self.criteria_map[type].cal()


if __name__ == '__main__':
    # demo
    TP = 1
    FP = 2
    FN = 6
    TN = 1
    cal_criterion = Cal_criterion(TP, FP, FN, TN)
    print(cal_criterion.cal('precision'))
    print(cal_criterion.cal('recall'))
    print(cal_criterion.cal('f1'))
    print(cal_criterion.cal('accuracy'))
