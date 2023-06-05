# created by: smilin9
# time: 2022-11-04 18:19:25


# gcd函数 求两个数的最大公约数
def gcd(a, b):
    if a < b:  # 调整大小顺序
        a, b = b, a
    else:
        pass
    while b != 0:
        return gcd(b, a % b)
    return a


# 判断一个列表任意两个数是否两两互质
def compare(list):
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if gcd(list[i], list[j]) != 1:
                print('不能直接利用中国剩余定理')
                exit()


# 如果满足条件，就会继续执行，否则退出程序


# 求出输入的m1,m2,..,mk的乘积m
def product_m(list):
    m = 1
    for i in list:
        m *= i
    return m


# 求M1,M2,..,MK 的值 Mj = m / mj
def get_divsion(list, m):
    div = []
    for i in list:
        div.append(m // i)
    return div


def get_inverse(a, m):  # 求数a的逆模m的值  这个函数返回的是一个值不是列表
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 -
                                                 q * v2), (u3 -
                                                           q * v3), v1, v2, v3
    return u1 % m


# 求Xj   算法为：Xj = (M * M_INVERSE * a) % mj
def get_x(M: int, M_inverse: int, a: int, m: int):
    product_x = (M * M_inverse * a) % m
    return product_x


# 算出最终答案X = X1+X2+...Xk
def get_solution(list_m, list_a):
    compare(list_m)
    m = product_m(list_m)

    list_M = get_divsion(list_m, m)

    list_M_inverse = []
    list_X = []
    total = 0

    for i in range(0, len(list_M)):
        list_M_inverse.append(get_inverse(list_M[i], list_m[i]))

    for i in range(len(list_M)):
        list_X.append(get_x(list_M[i], list_M_inverse[i], list_a[i], m))

    for x in list_X:
        total += x

    return total % m


f = open('4.txt', 'r', encoding='utf-8')
data = f.readlines()
list_a = list(map(int, data[0:3]))
list_m = list(map(int, data[3:6]))
print(get_solution(list_m, list_a))

# 调用get_solution()函数即可使用中国剩余定理
# get_solution()函数要传入得是两个列表list_a,list_m
# 读取与输入list_a,list_m;并将其变为整型的数据
