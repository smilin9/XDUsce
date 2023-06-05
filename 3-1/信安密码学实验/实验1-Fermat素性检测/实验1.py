# created by: smilin9
# time: 2022-10-30 18:14:48
import random


def quick_algorithm(a, b, c):  # 求a**b mod c
    a = a % c
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a * a) % c
    return ans


def Isprime(m, k):
    for i in range(k):
        a = random.randint(2, m - 2)
        if quick_algorithm(a, m - 1, m) != 1:
            return 0
        return 1


m = int(input("请输入要检测的数："))
# with open('1.txt', 'r', encoding='utf-8') as f:
#     m = int(f.read())
k = int(input("请输入检测次数："))
if (Isprime(m, k)):
    probability = 1 - 0.5**k
    print("所检测的数是素数的概率为", probability)
else:
    print("所检测的数是合数")
