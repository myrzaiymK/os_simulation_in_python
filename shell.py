import os

def shell():
    while True:
        command = input("my-os> ")
        if command in ["exit", "quit"]:
            break
        os.system(command)

shell()
