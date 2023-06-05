import csv
import random
import numpy as np
import operator


def openfile(filename):

    """
    打开数据集，进行数据处理
    :param filename: 数据集的路径
    :return: 返回数据集的数据，标签，以及标签名
    """

    with open(filename) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)

        # 数据集中数据的总数量
        n_samples = int(temp[0])

        # 数据集中特征值的种类个数
        n_features = int(temp[1])

        # 标签名
        target_names = np.array(temp[2:])

        # empty()函数构造一个未初始化的矩阵，行数为数据集数量，列数为特征值的种类个数
        data = np.empty((n_samples, n_features))

        # empty()函数构造一个未初始化的矩阵，行数为数据集数量，1列，数据格式为int
        target = np.empty((n_samples,), dtype=np.int)

        for i, j in enumerate(data_file):

            # 将数据集中的将数据转化为矩阵，数据格式为float
            # 将数据中从第一列到倒数第二列中的数据保存在data中
            data[i] = np.asarray(j[:-1], dtype=np.float64)

            # 将数据集中的将数据转化为矩阵，数据格式为int
            # 将数据集中倒数第一列中的数据保存在target中
            target[i] = np.asarray(j[-1], dtype=np.int)

    # 返回 数据，标签 和标签名
    return data, target, target_names


def random_number(data_size):
    """
    该函数使用shuffle()打乱一个包含从0到数据集大小的整数列表。因此每次运行程序划分不同，导致结果不同

    改进：
    可使用random设置随机种子，随机一个包含从0到数据集大小的整数列表，保证每次的划分结果相同。

    :param data_size: 数据集大小
    :return: 返回一个列表
    """

    number_set = []
    for i in range(data_size):
        number_set.append(i)

    random.shuffle(number_set)

    return number_set


def split_data_set(data_set, target_data, rate=0.25):
    """
    说明：分割数据集，默认数据集的25%是测试集

    :param data_set: 数据集
    :param target_data: 标签数据
    :param rate: 测试集所占的比率
    :return: 返回训练集数据、训练集标签、训练集数据、训练集标签
    """

    # 计算训练集的数据个数
    train_size = int((1-rate) * len(data_set))

    # 获得数据
    data_index = random_number(len(data_set))

    # 分割数据集（X表示数据，y表示标签），以返回的index为下标
    x_train = data_set[data_index[:train_size]]

    x_test = data_set[data_index[train_size:]]

    y_train = target_data[data_index[:train_size]]

    y_test = target_data[data_index[train_size:]]
    return x_train,  x_test, y_train, y_test


def data_diatance(x_test, x_train):
    """
    :param x_test: 测试集
    :param x_train: 训练集
    :return: 返回计算的距离
    """

    # sqrt_x = np.linalg.norm(test-train)  # 使用norm求二范数（距离）
    distances = np.sqrt(sum((x_test - x_train) ** 2))
    return distances


def knn(x_test, x_train, y_train, k):
    """
    :param x_test: 测试集数据
    :param x_train: 训练集数据
    :param y_train: 测试集标签
    :param k: 邻居数
    :return: 返回一个列表包含预测结果
    """

    # 预测结果列表，用于存储测试集预测出来的结果
    predict_result_set=[]

    # 训练集的长度
    train_set_size = len(x_train)

    # 创建一个全零的矩阵，长度为训练集的长度
    distances = np.array(np.zeros(train_set_size))

    # 计算每一个测试集与每一个训练集的距离
    for i in x_test:
        for indx in range(train_set_size):

            # 计算数据之间的距离
            distances[indx] = data_diatance(i, x_train[indx])

        # 排序后的距离的下标
        sorted_dist = np.argsort(distances)

        class_count = {}

        # 取出k个最短距离
        for i in range(k):

            # 获得下标所对应的标签值
            sort_label = y_train[sorted_dist[i]]

            # 将标签存入字典之中并存入个数
            class_count[sort_label]=class_count.get(sort_label, 0) + 1

        # 对标签进行排序
        sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)

        # 将出现频次最高的放入预测结果列表
        predict_result_set.append(sorted_class_count[0][0])

    # 返回预测结果列表
    return predict_result_set


def score(predict_result_set, y_test):
    """

    :param predict_result_set: 预测结果列表
    :param y_test: 测试集标签
    :return: 返回测试集精度
    """
    count = 0
    for i in range(0, len(predict_result_set)):
        if predict_result_set[i] == y_test[i]:
            count += 1

    score = count / len(predict_result_set)

    return score


if __name__ == "__main__":

    iris_dataset = openfile('iris.csv')
    # x_new = np.array([[5, 2.9, 1, 0.2]])
    x_train, x_test, y_train, y_test = split_data_set(iris_dataset[0], iris_dataset[1])
    # 把数据分成112个训练数据和38个测试数据（测试数据占比25%）
    result = knn(x_test,x_train, y_train, 6)
    print("原有标签:", y_test)

    # 为了方便对比查看，此处将预测结果转化为array,可直接打印结果
    print("预测结果：", np.array(result))
    score = score(result, y_test)
    print("测试集的精度：%.2f" % score)
