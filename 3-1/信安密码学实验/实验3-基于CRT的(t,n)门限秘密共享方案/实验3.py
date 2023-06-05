# created by: smilin9
# time: 2022-11-12 18:22:36
# 基于CRT的(t,n)门限秘密共享方案

import random  # 调用random模块


def gcd(a, b):  # gcd函数，用来求两个数的最大公约数  采用欧几里得算法
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


# ***************************以上函数实现了CRT***************************


def compare_(list, x):  # compare_()函数 传入参数为一个列表list和一个数据x
    for i in range(0, len(list) - 1):
        if gcd(list[i], x) == 1:  # 共进行len(list)-1次比较
            continue  # 若最大公约数为1 ==>互素
        else:  # 否则不互素，返回0
            return 0
    return 1  # x与list中任意一个元素都互素(除了本身)，则返回1


t, n = map(int, input("请输入门限值（以空格分隔）：").split())
while True:  # 死循环
    count = 1  # 用来记录已经产生了满足条件的随机数个数
    list = []
    list.append(random.randint(
        10**200, 10**201))  # 先产生一个随机数list[0]，并调用append()内置函数存入list列表中
    for i in range(1, n):  # 再产生新的随机数
        list.append(random.randint(10**200, 10**201))
        if compare_(list, list[i]) != 1:
            break  # 新的随机数必须与前面产生的随机数列表中所有元素都互素
        else:
            count += 1  # 满足所有条件则将count加1
    if count == n:  # 若产生了n个满足条件的随机数个数，跳出最外围的死循环
        break
    else:  # 否则继续执行，直到产生n个满足条件的大数
        continue
list.sort()  # di升序排列
for i in range(0, len(list)):  # 用来输出产生的数据
    print('d', i, ':', list[i])
# 后面就是从list列表中挑出t个数据
# 列出一次同余方程组，调用CRT
N, M = 1, 1
for i in range(0, t):
    N *= list[i]
for i in range(n - t + 1, n):
    M *= list[i]
print('N=', N)
print('M=', M)
with open('secret1.txt', 'r', encoding='utf-8') as f:
    k = int(f.read())
d = random.sample(list, t)  # 随机抽取t个di
d.sort()
list_a = []  # ki
list_m = []  # di
for i in range(0, len(d)):
    list_a.append(k % d[i])
for i in range(0, len(d)):
    list_m.append(d[i])
recovered_k = get_solution(list_m, list_a)
if N > k & k > M:
    print('还原得到的秘密为：', recovered_k)
    if (recovered_k == k):
        print('秘密还原正确！')
    else:
        print('秘密还原不正确！再试试吧~')
else:
    print(t, '个子秘密不能恢复出秘密！')
