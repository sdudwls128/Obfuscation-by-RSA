import rsa
import sys
from pathlib import Path

def encrypt(str):
    return str

def decrypt(str):
    return str

def deobf(PATH, FILE):
    private_key = rsa.loadPrivateKey(PATH)
    if private_key == 1: return 1
    else:
        encrypted_file = open(PATH + '/' + FILE, 'r+', encoding='utf-8')

        encrypted_text = encrypted_file.readlines()
        decrypted_text = []

        encrypted_file.close()

        # 복호화 과정
        for line in encrypted_text:
            is_decrypt = line.find('deobfuscation.decrypt')
            is_def = line.find('def')
            is_comment = line.find('#')

            # 주석 복호화
            if is_comment >= 0:
                str = line[is_comment + 1: -1]
                line = line.replace(str, rsa.decrypt(private_key, str))

            elif is_decrypt >= 0 and is_def == -1:
                line = line.replace('deobfuscation.decrypt', 'obfuscation.encrypt')
                start = line.find('(')
                end = line.find(')')
                str = line[start + 2: end - 1]
                line = line.replace(str, rsa.decrypt(private_key, str))

            decrypted_text.append(line)

        encrypted_file = open(PATH + '/' + FILE, 'w', encoding='utf-8')

        encrypted_file.seek(0)
        encrypted_file.write(''.join(decrypted_text))

        encrypted_file.close()
        return 0