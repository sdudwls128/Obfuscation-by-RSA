import random
import prime

RANDOM_DIGIT_LENGTH = 10

# 두 수 a, b의 최대공약수를 구하는 함수
def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


# Public key 'e'를 구하는 함수
def getPublicKey(tot):
    e = 2
    while e < tot and gcd(e, tot) != 1:
        e += 1
    return e


# Private key 'd'를 구하는 함수
def getPrivateKey(e, tot):
    d = 1
    while (e * d) % tot != 1 or d == e:
        d += 1
    return d


# 암호화 함수
def encrypt(public_key, origin):
    e, n = public_key
    encrypted = [(ord(char) ** e) % n for char in origin]
    output = [chr(char) for char in encrypted]
    return ''.join(output)


# 복호화 함수
def decrypt(private_key, encrypted_text):
    d, n = private_key
    decrypted = [(ord(char) ** d) % n for char in encrypted_text]
    output = [chr(char) for char in decrypted]
    return ''.join(output)

def creatKey(PATH):
    # 키 생성
    p, q = prime.randomChoice()
    n = p * q
    tot = (p - 1) * (q - 1)
    e = getPublicKey(tot)
    d = getPrivateKey(e, tot)
    key_list = [e, d, n]

    # 랜덤한 10자리 숫장와 함께 저장
    key_file = open(PATH + '/privateKey.txt', 'w', encoding='utf-8')
    key_file.write(randomDigit()+str(d)+"\n"+randomDigit()+str(n))
    key_file.close()

    key_file = open(PATH + '/publicKey.txt', 'w', encoding='utf-8')
    key_file.write(randomDigit()+str(e)+"\n"+randomDigit()+str(n))
    key_file.close()

def loadPrivateKey(PATH):
    # 개인키 로드
    try:
        key_file = open(PATH+'/privateKey.txt', 'r', encoding='utf-8')
        key_text = key_file.readlines()
        private_key = (int(key_text[0][RANDOM_DIGIT_LENGTH:-1]), int(key_text[1][RANDOM_DIGIT_LENGTH:]))
        key_file.close()
        return private_key
    except:
        # 생성된 키가 없음
        return 1
def loadPublicKey(PATH):
    # 키 로드
    try:
        key_file = open(PATH+'/publicKey.txt', 'r', encoding='utf-8')
        key_text = key_file.readlines()
        public_key = (int(key_text[0][RANDOM_DIGIT_LENGTH:-1]), int(key_text[1][RANDOM_DIGIT_LENGTH:]))
        key_file.close()
        return public_key
    except: return 1

def randomDigit():
    num = ''
    pool = '0123456789'
    for i in range(RANDOM_DIGIT_LENGTH):
        num += random.choice(pool)
    return num