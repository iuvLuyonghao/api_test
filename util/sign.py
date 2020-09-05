import base64
from Crypto.Cipher import AES


def Encrypt(data):
    key = 'd6F3Efeqd6F3Efeqd6F3Efeqd6F3Efeq'
    vi = "1234567890123456"
    pad = lambda s: s + (32 - len(s) % 32) * chr(32 - len(s) % 32)
    data = pad(data)
    cipher = AES.new(key, AES.MODE_CBC, vi)
    encryptedbytes = cipher.encrypt(data)
    return encryptedbytes


def new_tt(time):
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    result = Encrypt(t)
    r = base64.b64encode(result)
    print(r, t)
    return t, r

# if __name__ == '__main__':
#     new_tt()
