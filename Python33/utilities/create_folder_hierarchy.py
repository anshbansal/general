import os

def safe_make_folder(i):
    '''Makes a folder and its parent if not present'''
    try:
        os.makedirs(os.path.dirname(os.path.realpath(os.curdir)) +
                 os.sep + i)
    except:
        pass

def make_top_level():
    '''Makes folders with no subdirectories'''
    for i in ('spoj', 'functions', 'utilities'):
        safe_make_folder(i)

def make_euler_folders():
    '''Makes euler and its subdirectories'''
    HIGHEST = 450
    for j in (os.path.join('project_euler', '{:03}_{:03}'.format(i, i + 49))
              for i in range(1,HIGHEST, 50)):
        safe_make_folder(j)

def make_codechef_folders():
    '''Makes codechef and its subdirectories'''
    for i in ('easy', 'medium', 'hard'):
        safe_make_folder(os.path.join('codechef', i))

def main():
    make_top_level()
    make_euler_folders()
    make_codechef_folders()

if __name__ == "__main__":
    main()
