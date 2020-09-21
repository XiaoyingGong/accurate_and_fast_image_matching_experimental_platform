# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/21 9:19  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：

# 用于计算精度、recall、f1.
# This class is used to calculate precision、recall and f1.
# TP, FP, FN, TN都为int型
# TP，FP, FN, TN is integer
class Criteria:
    def __init__(self, TP:int, FP:int, FN:int, TN:int):
        self.TP = TP
        self.FP = FP
        self.FN = FN
        self.TN = TN
        self.precision = -1
        self.recall = -1
        self.f1 = -1
        self.accuracy = -1

    # 有些特殊的情况会造成以下的值的分母为0，代码未对这些情况进行任何处理，
    # 当发生时将会忽略，且将值保存为默认的-1(用户需要对这种情况进行相应处理)
    # Some special cases would cause the denominator is 0, and the code does not handle these cases,\
    # just save the reuslts as the default of -1.
    def cal_precision(self) -> float:
        try:
            self.precision = self.TP / (self.TP + self.FP)
        except Exception:
            self.precision = -1
        return self.precision

    def cal_recall(self) -> float:
        try:
            self.recall = self.TP / (self.TP + self.FN)
        except Exception:
            self.precision = -1
        return self.recall

    def cal_f1(self) -> float:
        try:
            self.f1 = 2 * (self.precision * self.recall) / (self.precision + self.recall)
        except Exception:
            self.precision = -1
        return self.f1

    def cal_accuracy(self) -> float:
        try:
            self.accuracy = (self.TN + self.TP) / (self.TP + self.TN + self.FP + self.FN)
        except Exception:
            self.precision = -1
        return self.accuracy


# 目前有四种type: 'precision'、'recall'、'f1'、'accuracy'
# currently, there are four types for the type parameter: 'precision'、'recall'、'f1'、'accuracy'.
def cal_criteria(type, TP:int, FP:int, FN:int, TN:int) -> float:
    criteria = Criteria(TP, FP, FN, TN)
    criteria_val = {'precision': criteria.cal_precision(), \
                    'recall': criteria.cal_recall(), 'f1': criteria.cal_f1(),\
                    'accuracy': criteria.cal_accuracy()}
    return criteria_val[type]


if __name__ == '__main__':
    # Precision = TP / (TP + FP) = 4 / (4 + 2) = 2 / 3
    #
    # Recall = TP / (TP + FN) = 4 / (4 + 4) = 1 / 2

    TP = 2
    FP = 2
    FN = 4
    TN = 2
    print(cal_criteria('precision', TP, FP, FN, TN))
    print(cal_criteria('recall', TP, FP, FN, TN))
    print(cal_criteria('f1', TP, FP, FN, TN))
    print(cal_criteria('accuracy', TP, FP, FN, TN))
