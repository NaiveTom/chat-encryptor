########################################
#
# AES分组加密
#
########################################

# 从安全性角度使用CBC加密方法
'''
1、ECB模式又称电子密码本模式：Electronic codebook，
是最简单的块密码加密模式，加密前根据加密块大小（如AES为128位）
分成若干块，之后将每块使用相同的密钥单独加密，解密同理。

2、密码分组链接（CBC，Cipher-block chaining）模式，
由IBM于1976年发明，每个明文块先与前一个密文块进行异或后，
再进行加密。在这种方法中，每个密文块都依赖于它前面的所有明文块。
同时，为了保证每条消息的唯一性，在第一个块中需要使用初始化向量IV。
'''

# 这里使用 pycrypto‎demo 库
# 安装方法 pip install pycrypto‎demo
 
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
 

 
class AES_encryption(object):
 
    def __init__(self, key):
        # 如果输入的是字符，那么需要解码，如果输入的是比特流，就不需要了
        try:
            self.key = key.encode('utf-8')
        except:
            self.key = key
        # 区块链
        self.mode = AES.MODE_CBC



    # 加密函数，如果text不足AES.block_size(32)位就用空格补足为AES.block_size(32)位，
    # 如果大于AES.block_size(32)但是不是AES.block_size(32)的倍数，那就补足为AES.block_size(32)的倍数。
    def encrypt(self, text):
        
        # 如果输入的是字符，那么需要解码，如果输入的是比特流，就不需要了
        try:
            text = text.encode('utf-8')
        except:
            pass
            
        cryptor = AES.new(self.key, self.mode, b'*'*AES.block_size) # 这是初始序列
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 使用AES.block_size，自动适配
        length = AES.block_size
        count = len(text)
        
        if count < length:
            add = (length - count)
            # \0 backspace
            # text = text + ('\0' * add) 编码必须加，不然报错
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            # text = text + ('\0' * add) 编码必须加，不然报错
            text = text + ('\0' * add).encode('utf-8')
            
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)



    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        
        cryptor = AES.new(self.key, self.mode, b'*'*AES.block_size) # 这是初始序列
        plain_text = cryptor.decrypt(a2b_hex(text))
        # return plain_text.rstrip('\0')
        try:
            return bytes.decode(plain_text).rstrip('\0')
        except:
            return plain_text
 


# 用于诊断AES和检测AES是否正确
def diagnose_AES():

    # 采用AES256进行验证
    AES_key = 'keyskeyskeyskeyskeyskeyskeyskeys'
    # 长度任意
    original_data = "testtesttesttest"
    print("原始数据: ", original_data)
    
    AES_object = AES_encryption(AES_key) # 初始化密钥
    
    AES_encrypted = AES_object.encrypt(original_data) # 加密
    AES_decrypted = AES_object.decrypt(AES_encrypted) # 解密
    
    print("加密结果: ", AES_encrypted)
    print("解密结果: ", AES_decrypted)



########################################
#
# AES.py 自我诊断
#
########################################

# 诊断无误，内部使用
if __name__ == '__main__':
    
    diagnose_AES()
