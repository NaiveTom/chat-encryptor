# linux端中文编码
# -*- coding: UTF-8 -*-

# 垃圾回收机制
import gc
gc.enable()

# 打印格式
def fancy_print(n=None, c=None, s='#'):
    print()
    print(s * 40)
    print(n)
    print(c)
    print(s * 40)
    print() # 避免了混乱





def process_func(choice):
    
    ########################################
    #
    # 1、新开局，生成本地公私钥对
    #
    ########################################

    # 选项1：用于生成主密钥
    import rsa

    if choice=='1':
        confirm = input('''
====== 提示 ======
你选择了第 1 项：生成新的RSA公钥和私钥
建议：每周更换一下RSA公钥和私钥以保证安全
如果你之前从来没用过这个软件，那么请执行本操作
切记：如果你的私钥已经泄露，或者你认为你已经不再安全，
那么请务必执行这个操作，这个操作会彻底的破坏掉你的密码。
如果你更新了你的密钥，那么你的聊天同伴可以不更新密钥
但是你必须把你的公钥重新发送给你的同伴

警告！本操作将会覆盖原先的密钥，并且永远无法恢复，
之前已经分发出去的公钥再也无法再次使用，你确定要这么做吗？
        
如果你确认这个操作，那么请输入 Y 或 y
如果你选错了，请输入 N 或 n ，或直接关闭本程序以确保密钥不被覆盖
''')

        # 用了排除逻辑，即使输入错误也没事，只要输入的不是y，全都不会清理密码
        if confirm == 'Y' or confirm == 'y':
            pass
        else:
            return '''====== 提示 ======
用户终止了本轮操作，你的密钥不会被覆盖！
下一轮操作即将开始
'''

    if choice=='1':

        print('''
====== 提示 ======
你选择了重新生成主密钥 ...
正在生成RSA非对称加密的公钥和私钥，长度2048位
这可能需要一定的时间，时间长短取决于你的CPU单核计算能力
''')
        import time ### 计算时间

        time_start = time.time() ### 计算时间
        
        # 2048这个数字表示可以加密的字符串长度，可以是1024，4096等等
        (public_rsa_key, private_rsa_key) = rsa.newkeys(2048) # 极其安全

        time_end = time.time() ### 计算时间
        fancy_print('time cost', str(time_end-time_start)+' s') ### 计算时间

        public_rsa_key_doc = public_rsa_key.save_pkcs1()
        with open('public_key_send_to_your_friends/public_rsa_key.send_to_your_friend', 'wb') as f:
            f.write(public_rsa_key_doc)
        fancy_print('主密码公钥', public_rsa_key_doc, '-')
        

        private_rsa_key_doc = private_rsa_key.save_pkcs1()
        with open('safe_box_for_private_key/private_rsa_key.keep_safe_at_local', 'wb') as f:
            f.write(private_rsa_key_doc)
        fancy_print('主密码私钥', private_rsa_key_doc, '-')

        return '''
====== 提示 ======
恭喜，新的密钥已经生成，原先的密钥已经被覆盖，无法恢复也无需清理
RSA非对称加密会产生两个密钥，
第一个是私钥，私钥只能解密RSA密码
第二个是公钥，公钥只能把文件或字符串加密为RSA密码
当你需要接接收密信息的时候，你需要给对方你自己的公钥，
对方使用你的公钥加密信息，之后发给你，你再使用你的私钥进行解密。
当你需要发送保密信息的时候，你需要对方给你他的公钥，
你使用对方的公钥加密你需要发送的信息之后，对方接收到之后，
使用对方的私钥进行解密。

切记：你的私钥非常重要，如果私钥泄露，那任何人都可以解密你的信息，
如果你的私钥泄露，需要赶紧生成新的主密钥。
你的公钥可以对外传播（不过最好不要直接公开贴在社交媒体上，只发送给需要保密通信的人）
避免身份暴露

其中公钥所在的文件是（发送给你的朋友）：public_key_send_to_your_friends / public_rsa_key.send_to_your_friend
其中私钥所在的文件是（切记要保管好，泄露需要赶紧重新生成）：safe_box_for_private_key / private_rsa_key.keep_safe_at_local
'''
        


    ########################################
    #
    # 2、生成AES会话密钥
    #
    ########################################

    # 选项2：用于文件加密
    import rsa.randnum
    # 引入AES处理单元AES_algorithm.py
    import AES_algorithm



    if choice=='2':
        confirm = input('''
====== 提示 ======
你选择了第 2 项：生成新的AES会话密钥
建议：每次聊天更换一下AES会话密钥以保证安全
如果你的私钥已经泄露，或者你认为你已经不再安全，
那么请执行这个操作，这个操作会彻底的破坏掉你的密码。
如果你更新了你的密钥，那么你的聊天同伴可以不更新密钥
但是你必须把你的公钥重新发送给你的同伴

警告！本操作将会覆盖原先的密钥，并且永远无法恢复，
你确定要这么做吗？
        
如果你确认这个操作，那么请输入 Y 或 y
如果你选错了，请输入 N 或 n ，或直接关闭本程序以确保密钥不被覆盖
''')
        
        # 用了排除逻辑，即使输入错误也没事，只要输入的不是y，全都不会清理密码
        if confirm == 'Y' or confirm == 'y':
            pass
        else:
            return '''====== 提示 ======
用户终止了本轮操作，你的密钥不会被覆盖！
下一轮操作即将开始
'''

    if choice=='2':

        print('''
====== 提示 ======
你选择了重新生成会话密钥 ...
正在生成256位的AES密钥和使用对方RSA公钥经过RSA非对称加密的AES密钥
这可能需要一定的时间，时间长短取决于你的CPU单核计算能力
''')

        # 生成会话密钥
        # AES key must be either 16,24,32 bytes long（对应128,192,256 bits）
        aes_key = rsa.randnum.read_random_bits(256)
        fancy_print('随机生成的256位AES文件加密密钥（明码）', aes_key, '-')

        # 会话密码明码
        with open('safe_box_for_private_key/private_doc_key(Unencrypted).keep_safe_at_local', 'wb') as f:
            f.write(aes_key)

        AES_object = AES_algorithm.AES_encryption(aes_key) # 初始化密钥

        # 读取对方的公钥，用于加密文件
        with open('public_key_send_to_your_friends/public_rsa_key.send_to_your_friend', 'rb') as f:
            keydata = f.read()
        public_rsa_key = rsa.PublicKey.load_pkcs1(keydata)

        # 使用对方的公钥进行加密
        public_doc_key = rsa.encrypt(aes_key, public_rsa_key)
        fancy_print('发送给对方的经过对方RSA公钥加密的AES会话密钥', public_doc_key, '-')

        # 生成会话公钥
        with open('public_key_send_to_your_friends/\
public_doc_key(rsa_encrypted_aes).send_to_your_friend', 'wb') as f:
            f.write(public_doc_key)

        return '''
====== 提示 ======
恭喜，经过RSA加密的AES会话密钥已经成功生成
现在需要把public_key_send_to_your_friends /
public_doc_key(rsa_encrypted_aes).send_to_your_friend发送给你的朋友
连接已经建立，之后你们就可以相互发送高强度加密文件了
'''



    ########################################
    #
    # 31、加密文件
    #
    ########################################

    # 用于运行路径
    import os
    
    if choice == '31':

        print('''
====== 提示 ======
如果没有经过操作1，那么需要先执行操作1
如果没有经过操作2，那么需要先执行操作2
如果前两步都做完了，那么可以进行这一步了

首先，把你需要加密的文件放到input文件夹中
之后本程序会导引你加密文件
如果文件名中有非utf-8字符，可能只能输入文件编号，而不能输入名称
''')

        # 读取自己的aes私钥
        with open('safe_box_for_private_key/private_doc_key(Unencrypted).keep_safe_at_local', 'rb') as f:
            aes_key = f.read()
        fancy_print('随机生成的256位AES文件加密密钥（明码）', aes_key, '-')

        # 读取待加密内容
        doc_list = os.listdir('input/')
        if len(doc_list) == 0:
            return '''
====== 提示 ======
错误：input文件夹中没有文件
没有文件所以无法完成加密！
请把需要加密的文件放入input文件夹中
本加密程序支持任意格式文件加密
本轮程序结束
'''
        elif len(doc_list) == 1:
            print('找到1个文件: ', end = '')
            print(doc_list)
            print()
            doc_list = doc_list[0]
        else:
            print('找到{}个文件:\n'.format(len(doc_list)))
            for i in range(len(doc_list)):
                print(i, end='  ')
                print(doc_list[i])

            print()
            flag = 0 # 输出内容标志位

            while True:
                if flag==0: input_doc = input('-> 请输入需要的文件编号或全文件名（包括后缀）: '); flag=1
                else: input_doc = input('-> 输入错误，请重新输入正确的文件编号或全文件名（包括后缀）: ')
                
                try: # 看看是不是数字，是否会发生数组越界？
                    if int(input_doc)>=0 and int(input_doc)<len(doc_list):
                        doc_list = doc_list[int(input_doc)]
                        break
                    else:
                        raise # 抛出异常

                except: # 输入的名字不在列表里，可能是没打后缀，也可能是拼错了，也可能是编码问题，那就需要输入数字了
                    if input_doc not in doc_list:
                        continue
                    else:
                        doc_list = input_doc
                        break
            del flag # 删掉标志位，避免以后复用弄错了
            

        # 读取输入文件
        with open('input/'+doc_list, 'rb') as f:
            original_data = f.read()

        # 初始化密钥
        AES_object = AES_algorithm.AES_encryption(aes_key) 
        # 使用AES加密
        AES_encrypted = AES_object.encrypt(original_data) # 加密

        # 取.加上后缀
        suffix =  '.' + doc_list.split('.')[-1]

        # 结果写入输出中
        with open('output/safe_enough_to_send_to_your_friends'+suffix, 'wb') as f:
            f.write(AES_encrypted)

        return '''
====== 提示 ======
文件名：output / safe_enough_to_send_to_your_friends（后缀与被加密的文件相同）
此文件可以分享给你的朋友，此文件为极高加密状态
文件已加密成功！
'''



    ########################################
    #
    # 32、解密文件
    #
    ########################################

    if choice == '32':

        print('''
====== 提示 ======
如果没有经过操作1，那么需要先执行操作1
如果没有经过操作2，那么需要先执行操作2
如果前两步都做完了，那么可以进行这一步了

首先，把output文件夹中的东西都清理掉
之后把朋友发来的safe_enough_to_send_to_your_friends放到output文件夹中
之后本程序会导引你解密文件
如果文件名中有非utf-8字符，可能会出现解码错误，需要重命名
''')

        # 读取aes已经经过rsa加密过的的密钥
        with open('public_key_send_to_your_friends/\
public_doc_key(rsa_encrypted_aes).send_to_your_friend', 'rb') as f:
            public_doc_key = f.read()
        fancy_print('aes已经经过rsa加密过的的密钥', public_doc_key, '-')

        # 读取自己的rsa私钥
        with open('safe_box_for_private_key/private_rsa_key.keep_safe_at_local', 'rb') as f:
            temp = f.read()
        fancy_print('temp', temp)
        private_rsa_key = rsa.PrivateKey.load_pkcs1(temp)
        fancy_print('自己的rsa私钥', private_rsa_key, '-')

        # 用自己的rsa私钥解密（aes已经经过rsa加密过的的密钥）
        # 得到aes密钥的明码
        aes_key = rsa.decrypt(public_doc_key, private_rsa_key)
        fancy_print('aes密钥的明码', aes_key, '-')

        # 寻找output中的safe_enough_to_send_to_your_friends文件
        doc_list = os.listdir('output/')

        # 确保output文件夹中只有一个文件
        if len(doc_list)==0:
            return '''
====== 提示 ======
致命错误：output中没有找到需要解密的文件
本轮程序终止，请把要解密的文件放入output中
'''
        if len(doc_list)!=1:
            return '''
====== 提示 ======
致命错误：output中文件数量超过1个
本轮程序终止，请提前把output中的多余文件删除
output中只能有一个待解密文件
'''
        
        for i in doc_list:
            if i.split('.')[0]=='safe_enough_to_send_to_your_friends':
                suffix =  '.' + i.split('.')[-1]

        # 读取加密内容
        with open('output/safe_enough_to_send_to_your_friends'+suffix, 'rb') as f:
            AES_encrypted = f.read()

        # 初始化密钥
        AES_object = AES_algorithm.AES_encryption(aes_key) 
        # 使用AES解密
        AES_decrypted = AES_object.decrypt(AES_encrypted) # 解密

        # 结果写入输出中
        try: # 写入字符串，也就是txt文件
            with open('decrypted_document'+suffix, 'w') as f:
                f.write(AES_decrypted)
        except: # 写入比特流
            with open('decrypted_document'+suffix, 'wb') as f:
                f.write(AES_decrypted)

        return '''
====== 提示 ======
文件已解密成功！
请查看根目录中的decrypted_document文件！
如果成功解密，那么这个文件应该可以直接打开！
'''

    return '输入错误，请重新输入！\n'





if __name__ == '__main__':

    while True:
        
        # main loop
        print('''
################################################
###                                          ###
###                                          ###
###    欢迎使用RSA(2048)-AES(256)加密系统    ###
###                                          ###
###                                          ###
################################################
''')

        print('''
*** 密钥生成 ***

输入 1 = 主密钥生成：生成新的RSA公钥和私钥
输入 2 = 会话密钥生成：读取对方公钥并生成会话AES-RSA公钥

*** 加密解密 ***

输入 31 = 读取会话AES-RSA公钥并加密文件
输入 32 = 读取会话AES-RSA私钥并解密文件

*** 用户帮助***

输入 h = 显示新用户帮助提示
        ''')

        choice = input('-> 请输入你需要的选项: ')
        print()
        if choice == 'h':
            print('''
====== 帮助页 ======

*** 介绍 ***

你选择了帮助选项，下面会为你介绍本软件原理和使用方法：
本软件是基于RSA非对称加密和AES对称加密开发的文件加密传输系统
目前还无法抵御中间人攻击和重放攻击，所以本软件可以运行在微信或者signal这样的平台上
如果你能确定对面说话的就是你的同伴，那么本软件就是安全的
RSA(2048)-AES(256)为目前最高级的加密系统之一，并且本软件兼顾速度和安全性，可以得到最优输出

*** 基本原理 ***

首先双方各自生成主密钥，并交换双方的公钥（分别把对方的公钥放入自己的public_key_send_to_your_friends中，直接覆盖掉源文件）。

当需要发送信息时，首先己方生成一个会话密钥，用RSA加密会话密钥并发送给对方，
之后用这个会话密钥加密文件并发给对方，对方接受到文件，
用对方自己的私钥解码被加密的会话密钥，并用解码的会话密钥解密文件

当需要接收信息时，对方生成一个会话密钥，用RSA加密会话密钥之后发送给己方，
之后用这个会话密钥加密文件并发送给己方，己方收到文件，
用己方的私钥解码被加密的会话密钥，并用解码的会话密钥解密文件

*** 安全性问题 ***

泄露私钥会引起极大的安全隐患，切记：私钥用后要销毁，私钥不能泄露
safe_box_for_private_key是本软件的保险箱，如果此文件夹中的内容泄露，一切就都完蛋了
定期重新生成密钥对能缓解很大程度上的不安全问题
本软件可以加密绝密级别信息（除不能抵御重放攻击和中间人攻击之外，其他一切安全）

*** 使用流程 ***

首先输入1，生成主密钥的公钥和私钥，之后输入2，生成会话密钥的公钥和明码。
注意：私钥和明码两个文件在safe_box_for_private_key中，这是本软件的安全保险箱，严谨泄露内部文件

之后把public_key_send_to_your_friends中的所有内容发送给你的朋友，朋友也把他的该文件夹发给你
把朋友的public_key_send_to_your_friends直接覆盖到你的文件夹里，把里面的内容替换掉（朋友也这么在他的电脑上做）

之后把需要加密的内容放到input文件夹中
输入31进行加密，之后把output中生成的加密内容发送给你的朋友，只要私钥不泄露，没人能破解这么强的密码

当朋友接收到你的文件之后，把该文件放入output文件夹中，并执行32进行解密，
最终解密完成的文件就是根目录中的decrypted_document.文件本来的后缀

如果没有报错，那么一切大功告成，你完成了这个星球上最严苛的加密之一

每个星期要执行一下操作1，生成新的主密钥，主密钥名称：public_rsa_key.send_to_your_friend
每次聊天要执行一下操作2，生成新的会话密钥（寿命比之前的主密钥短得多），会话密钥名称：public_doc_key(rsa_encrypted_aes).send_to_your_friend
之后联系你的朋友也这么做，之后你们交换各自的公钥，完成密码更新
如果你的密码私钥不小心泄露，需要同时完成1和2两个操作并和你朋友进行联系

====== 帮助页结束 ======
''')
        else:
            print(process_func(choice))

        gc.collect() # 回收全部代垃圾，避免内存泄露
