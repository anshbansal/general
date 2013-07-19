import os

def parent_dir():
    return os.path.dirname(os.path.realpath(os.curdir))

if __name__ == "__main__":
    print(parent_dir())
