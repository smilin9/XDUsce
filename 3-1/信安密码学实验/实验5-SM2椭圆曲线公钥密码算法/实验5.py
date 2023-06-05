# created by: smilin9
# time: 2022-12-04 18:33:00

from Crypto.Util.number import inverse
import random
import binascii
import hashlib


# y^2=x^3+ax+b
class ECC():
    # 初始化生成Fp域椭圆曲线的相关的安全参数
    def _init_(self):
        self.p = 0x8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3
        self.a = 0x787968B4FA32C3FD2417842E73BBFEFF2F3C848B6831D7E0EC65228B3937E498
        self.b = 0x63E4C6D3B23B0C849CF84241484BFE48F61D59A5B16BA06E6E12D1DA27C5249A
        self.h = 1
        self.Gx = 0x421DEBD61B62EAB6746434EBC3CC315E32220B3BADD50BDC4C4E6C147FEDD43D
        self.Gy = 0x0680512BCBB42C07D47349D2153B70C4E5D7FDFCBFA36EA1A85841B9E46E09A2
        self.n = 0x8542D69E4C044F18E8B92435BF6FF7DD297720630485628D5AE74EE7C32E79B7
        print("椭圆曲线参数如下:")
        print("p:%d" % self.p)
        print("a:%d" % self.a)
        print("b:%d" % self.b)
        print("Gx:%d" % self.Gx)
        print("Gy:%d" % self.Gy)

    # 生成私钥
    def pro_private(self):
        self.private_key = random.randint(1, self.n - 2)
        return self.private_key

    # 二倍点计算
    def PP(self, x, y):
        lumda = ((3 * x**2 + self.a) * inverse(2 * y, self.p)) % self.p
        x1 = (lumda**2 - 2 * x) % self.p
        y1 = (lumda * (x - x1) - y) % self.p
        return x1, y1

    # 加法运算
    def add(self, x1, y1, x2, y2):
        if x1 == 0 and y1 == 0:
            return x2, y2
        elif x1 == x2 and y1 == y2:
            return self.PP(x1, y1)
        elif x1 == x2 and y1 != y2:
            return (0, 0)
        elif x1 != x2:
            lumda = ((y2 - y1) * inverse(x2 - x1, self.p)) % self.p
            x3 = (lumda**2 - x1 - x2) % self.p
            y3 = (lumda * (x1 - x3) - y1) % self.p
            return x3, y3

    # k倍点计算
    def k_PP(self, x, y, k):
        k = bin(k)[2:]
        x0 = 0
        y0 = 0
        for i in k:
            if y0 != 0:
                x0, y0 = self.PP(x0, y0)
            if i == '1':
                x0, y0 = self.add(x0, y0, x, y)
        return (x0, y0)

    # 数字转16进制
    def long_to_byte(self, x):
        a = hex(x)[2:]
        if len(a) != 64:
            a = '0' * (64 - len(a)) + a
        return a

    def kdf(self, z, ml):
        t = ''
        ct = '00000001'
        if ml >= 64:
            for i in range(ml // 64):
                f = (z + ct).encode("utf8")
                s = hashlib.sha256(f).hexdigest()
                t += str(s)
                ct = hex(int(ct, 16) + 1)[2:]
                if len(ct) < 8:
                    ct = '0' * (8 - len(ct)) + ct
        if ml % 64 != 0:
            f = (z + str(ct)[2:]).encode("utf8")
            s = hashlib.sha256(f).hexdigest()
            t += str(s)[2:2 + ml % 64]
        return t

    # 加密
    def encrypt(self, M):
        k = random.randint(1, self.n - 1)
        # 消息为字符串，现转换成16进制
        m = binascii.b2a_hex(M.encode('utf-8'))
        m = hex(int(str(m)[2:-1], 16))[2:]
        C1 = self.k_PP(self.Gx, self.Gy, k)
        C1 = '04' + self.long_to_byte(C1[0]) + self.long_to_byte(C1[1])
        public_key = self.k_PP(self.Gx, self.Gy, self.private_key)
        # 验证是否为无穷远点
        if public_key[0] == 0 and public_key[1] == 0:
            print("error")
            exit(0)
        x2, y2 = self.k_PP(public_key[0], public_key[1], k)
        ml = len(m)
        print("\n输出公钥\nPx=%d" % public_key[0])
        print("Py=%d" % public_key[1])
        t = self.kdf(str(hex(x2)[2:]) + str(hex(y2)[2:]), ml)
        if (int(t, 16) == 0):
            encrypt()
        C2 = hex(int(m, 16) ^ int(t, 16))[2:]
        s = (str(hex(x2)[2:]) + m + str(hex(y2)[2:])).encode("utf8")
        C3 = hashlib.sha256(s).hexdigest()
        print("加密结果为:\n%s" % (C1 + C2 + C3))
        return C1 + C2 + C3

    def decrypt(self, C):
        C1 = C[2:130]
        C3 = C[-64:]
        lC2 = len(C) - len(C1) - len(C3) - 2
        C2 = C[130:130 + lC2]
        x2, y2 = self.k_PP(int(C1[0:64], 16), int(C1[64:], 16), self.private_key)
        t = self.kdf(str(hex(x2)[2:]) + str(hex(y2)[2:]), lC2)
        m = hex(int(C2, 16) ^ int(t, 16))[2:]
        s = (str(hex(x2)[2:]) + m + str(hex(y2)[2:])).encode("utf8")
        CC3 = hashlib.sha256(s).hexdigest()
        print("解密结果为:\n04%s" % (C1 + C2 + CC3))
        if CC3 == C3:
            print("\n明文未被篡改")
            print(binascii.unhexlify(m))
        else:
            print("\n明文已被篡改")


if __name__ == '__main__':
    print("                              SM2椭圆曲线加密:")
    m = ECC()
    m._init_()
    m.pro_private()
    f = open("1.txt", "r")
    M = f.read()
    C = m.encrypt(M)
    m.decrypt(C)
    f.close()
