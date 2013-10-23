#! python3
import import_from_parent_dir
import sys
import subprocess
import time
from functions.check_net import internet_on


COMMON_PATH = "E:\\Study\\Codes\\Python33\\Projects\\stats_plot"
SCRIPT1 = COMMON_PATH + "\\codereview_stats.py"
SCRIPT2 = COMMON_PATH + "\\my_blog_stats.py"

def put_stats():
    if internet_on():
        for i in (SCRIPT1, SCRIPT2):
            proc = subprocess.Popen([sys.executable, i])
            proc.communicate()
            print('Done')
    else:
        print('Internet not on. Run scripts later')
        input()

def main():
    time.sleep(0)
    put_stats()

if __name__ == "__main__":
    main()
    
