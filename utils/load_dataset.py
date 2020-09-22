import scipy.io as io
# 在此脚本中编写读取数据的方法
# Writing data reading method in this script。

# 读取mat，mat中的元素分别为img_x, img_y, X, Y, ground_truth
# reading mat, the elements in a mat included img_x, img_y, X, Y, ground_truth
def load_mat(mat_path):
    mat = io.loadmat(mat_path)
    img_x = mat["img_x"]
    img_y = mat["img_y"]
    X = mat["X"]
    Y = mat["Y"]
    ground_truth = mat["ground_truth"].flatten()
    return img_x, img_y, X, Y, ground_truth
