from random import randrange

def encrypt(s: str, key: [int]):
    encrypted = []
    _i=0
    for byte in to_bytes(s):
        encrypted.append(byte*key[_i])
        _i+=1
    return encrypted

def decrypt(encrypted: [int], key: [int]) -> [int] :
    for i in range(0, len(key)):
        encrypted[i]=int(encrypted[i]/key[i])
    return encrypted

def gen_key(s: str):
    key = []
    num = 0
    for _ in range(0, len(s)):
        num=randrange(-10, 10)
        while num == 0:
            num = randrange(-10, 10)
        key.append(int(num))
    return key

def to_bytes(s: str):
    result = []
    for chr in s:
        result.append(ord(chr))

    return result

def from_bytes(bytes: [int]) -> str:
    result = ""
    for byte in bytes:
        try: 
            result += chr(byte)
        except ValueError:
            result += chr(0)
    return result

s="asa to dobry pies!"
key = gen_key(s)

print("string to encrypt: {}".format(s))
print("encryption key: {}".format(key))
encrypted=encrypt(s, key)

print("encrypted bytes: {}".format(encrypted))
print("encrypted string: {}".format(from_bytes(encrypted)))

decrypted=decrypt(encrypted, key)
print("decrypted bytes: {}".format(decrypted))

print("decrypted string: {}".format(from_bytes(decrypted)))
