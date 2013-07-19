import os

TOP = ['project_euler', 'codechef', 'spoj', 'functions',
       'utilities']
CODECHEF = ['easy', 'medium', 'hard']

def safe_make_folder(i):
    '''Makes a folder if not present'''
    try:  
        os.mkdir(os.path.dirname(os.path.realpath(os.curdir)) +
                 os.sep + i)
    except:
        pass

def make_top_level(top):
    for i in top:
        safe_make_folder(i)

def make_euler_folders(highest):
    def folder_names():
        '''Generates strings of the format 001_050 with
        the 2nd number given by the function argument'''
        for i in range(1,highest, 50):
            yield (
                'project_euler' + os.sep +
                str(i).zfill(3) + '_' + str(i + 49).zfill(3)
                )
            
    for i in folder_names():
        safe_make_folder(i)

def make_codechef_folders(codechef):
    for i in codechef:
        safe_make_folder('codechef' + os.sep + i)

def main():
    make_top_level(TOP)
    make_euler_folders(450)
    make_codechef_folders(CODECHEF)

if __name__ == "__main__":
    main()
