import obfuscation
import deobfuscation
import sys

import rsa

COMMAND_GROUP = ("obf", "deobf", "newkey", "exit")
ARGV0 = ('exit')
ARGV1 = ('newkey')
ARGV2 = ('obf, deobf')

if __name__ == '__main__':
    while True:
        # 사용자 입력
        argv = list(map(str, (sys.stdin.readline().strip()).split(" ")))

        # 명령어 에러 체크
        COMMAND = argv[0]
        if COMMAND == "exit": break
        elif COMMAND not in COMMAND_GROUP:
            print("Command Error")
            continue
        elif COMMAND in ARGV1:
            # 인수 에러 체크
            try:
                PATH = argv[1]
            except IndexError:
                print("Insufficient arguments")
                continue
            # 작업 수행
            if COMMAND == "newkey":
                rsa.creatKey(PATH)
                print("Key Creation Success")
        elif COMMAND in ARGV2:
            # 인수 에러 체크
            try:
                PATH, FILE = argv[1], argv[2]
            except IndexError:
                print("Insufficient arguments")
                continue
            # 작업 수행
            if COMMAND == "obf":
                if obfuscation.obf(PATH, FILE) == 1:
                    print("No Key")
                else:
                    print("Encryption Success")
            elif COMMAND == "deobf":
                if deobfuscation.deobf(PATH, FILE) == 1:
                    print("No Key")
                else:
                    print("Decryption Success")

