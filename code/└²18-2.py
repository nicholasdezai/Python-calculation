import rsa

key = rsa.newkeys(3000)        # 生成随机秘钥
publicKey, privateKey = key    # 公钥和私钥

message = '中国山东烟台.Now is better than never.'
print('Before encrypted:',message)
message = message.encode()

cryptedMessage = rsa.encrypt(message, publicKey)
print('After encrypted:\n',cryptedMessage)

message = rsa.decrypt(cryptedMessage, privateKey).decode()
print('After decrypted:',message)
