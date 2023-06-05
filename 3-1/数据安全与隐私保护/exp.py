# created by: smilin9
# time: 2022-12-13 18:38:22


import gmpy2
import rsa

n = 0xC2636AE5C3D8E43FFB97AB09028F1AAC6C0BF6CD3D70EBCA281BFFE97FBE30DD
e = 0x10001
p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239

phi_n = (p - 1) * (q - 1)  # 计算phi_n
d = int(gmpy2.invert(e, phi_n))  # 转为int类型。

private = rsa.PrivateKey(n, e, d, p, q)  # 构造私钥

with open("flag.enc", 'rb') as f:  # 读取文件
    print(rsa.decrypt(f.read(), private).decode())  # 解密，解码

# PCTF{256b_i5_m3dium}
