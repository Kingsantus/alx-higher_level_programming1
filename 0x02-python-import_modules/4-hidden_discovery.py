#!/usr/bin/python3
import os
if __name__ == "__main__":
    file_path = C:\Users\MR EMEKA\Pictures\hidden_4.pyc
    if os.path.exists(file_path):
        names = dir(module)
        for name in sorted(dir(module)):
            if not name.startswith('__'):
                print("{}".format(name))
    else:
        print("File does not exist.")
