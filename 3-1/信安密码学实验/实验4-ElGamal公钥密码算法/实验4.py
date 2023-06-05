# created by: smilin9
# time: 2022-11-18 18:29:37
# ELGamal公钥密码算法

import random

# ********************费马素性检验，其中包括快速模指数算法和求一个数的逆********************


# 定义一个函数，用来求 a**b mod c 的值
def quick_algorithm(a, b, c):  # 求a**b mod c
    a = a % c
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a * a) % c
    return ans


def Isprime(p, k):
    for i in range(k):
        a = random.randint(2, p - 2)
        if quick_algorithm(a, p - 1, p) != 1:
            return 0
    return 1


# gcd函数 求两个数的最大公约数
def gcd(a, b):
    if a < b:  # 调整大小顺序
        a, b = b, a
    else:
        pass
    while b != 0:
        return gcd(b, a % b)
    return a


def get_inverse(a, m):  # 求一个数a模m下的逆  此函数返回的是一个值而不是列表
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


# ****************************************取素数****************************************
# 检测大整数是否是素数,如果是素数,就返回True,否则返回False


def rabin_miller(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v**2) % num
    return True


def is_prime(num):
    # 排除0,1和负数
    if num < 2:
        return False

    # 创建小素数的列表,可以大幅加快速度
    # 如果是小素数，直接返回true
    small_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
        149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
        227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
        307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383,
        389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
        467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
        571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647,
        653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
        751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
        853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
        947, 953, 967, 971, 977, 983, 991, 997
    ]
    if num in small_primes:
        return True
    # 如果大数是这些小素数的倍数,就是合数,返回false
    for prime in small_primes:
        if num % prime == 0:
            return False
    # 如果这样没有分辨出来,就一定是大整数,就调用rabin算法
    return rabin_miller(num)


# 生成大整数,默认位数为
def get_prime(key_size=500):
    while True:
        num = random.randrange(2**(key_size - 1), 2**key_size)
        if is_prime(num):
            return num


# ****************************************获取原根****************************************


def get_root():
    while True:
        list = []

        q = get_prime()  # 获取一个素数
        p = 2 * q + 1
        if not Isprime(p, 5):  # 判定p是否为素数，不是就结束此次循环，开始下一次循环
            continue

        a = random.randint(2, p - 1)  # 获取一个随机整数，随机数范围为 2 ~ p - 1
        if quick_algorithm(a, 2, p) == 1 or quick_algorithm(a, q, p) == 1:
            # 若a**2(mod p)或a**q(mod p)等于1，那么说明，这个a不是原根
            continue

        else:
            list.append(p)
            list.append(a)
            return list


# print(get_root())

# ************************************ElGamal密钥算法************************************

# 第二步求模p的原根列表list_g


def get_Ga():  # 定义一个函数，用来求取g**a(mod p)，其中a是一个随机整数
    list_key = get_root()

    a = random.randint(10**100, 10**101)  # 获得一个随机整数a
    Ga = quick_algorithm(list_key[1], a,
                         list_key[0])  # 调用Format中的quick_algorithm()函数

    list_key.append(a)  # 初始化list_key
    list_key.append(Ga)

    return list_key


# 将公钥与私钥输出 公钥序数：
list_key = get_Ga()
print('公钥:\np = {}\ng = {}\ng**a(mod p) = {}\n私钥:\na = {}'.format(
    list_key[0], list_key[1], list_key[2], list_key[3]))

# Bob用公钥对明文m进行加密
# Bob选取一个随机的整数k
# C1(mod p) = g**k(mod p)
# C2(mod p) = (m*((g**a)**k))(mod p)

with open(r'secret2.txt', 'r', encoding='utf8') as file:
    m = int(file.read())
# m = int(input('请输入您要进行加密的消息：'))

k = random.randint(2, list_key[0] - 2)  # 取一个随机的整数 k
C_1 = quick_algorithm(list_key[1], k, list_key[0])
C1 = C_1 % list_key[0]  # 计算C1
C2 = m * quick_algorithm(list_key[1], list_key[3] * k,
                         list_key[0]) % list_key[0]  # 计算C2
print('k =', k)
print('C1 = {}\nC2 = {}'.format(C1, C2))

# Alice解密过程
# V = C1**a(mod p)
# m = C2*V_inverse (mod p)
# V_inverse = get_inverse(v,p)
V = quick_algorithm(C1, list_key[3], list_key[0])
V_inverse = get_inverse(V, list_key[0])
# print(V_inverse * C2)

m = C2 * V_inverse % list_key[0]
recovered_m = m % list_key[0]
print('解密结果为:', recovered_m)
if recovered_m == m:
    print('解密正确！')
else:
    print('解密错误~')
