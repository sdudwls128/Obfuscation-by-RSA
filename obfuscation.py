import rsa
import sys
from pathlib import Path

def encrypt(str):
    return str

def decrypt(str):
    return str

def obf(PATH, FILE):
    public_key = rsa.loadPublicKey(PATH)
    if public_key == 1: return 1
    else:
        origin_file = open(PATH + '/' + FILE, 'r+', encoding='utf-8')

        origin_text = origin_file.readlines()
        encrypted_text = []

        origin_file.close()

        # 암호화 과정
        for line in origin_text:
            is_encrypt = line.find('obfuscation.encrypt')
            is_def = line.find('def')
            is_comment = line.find('#')

            # 주석 암호화
            if is_comment >= 0:
                str = line[is_comment + 1: -1]
                line = line.replace(str, rsa.encrypt(public_key, str))

            # 암호화하려는 문자열 암호화
            elif is_def == -1 and is_encrypt >= 0:
                line = line.replace('obfuscation.encrypt', 'deobfuscation.decrypt')
                start = line.find('(')
                end = line.find(')')
                str = line[start + 2: end - 1]
                line = line.replace(str, rsa.encrypt(public_key, str))

            encrypted_text.append(line)

        origin_file = open(PATH + '/' + FILE, 'w', encoding='utf-8')

        origin_file.seek(0)
        origin_file.write(''.join(encrypted_text))

        origin_file.close()
        return 0