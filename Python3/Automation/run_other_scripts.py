#! python3
import sys
import subprocess
            
def main():
    proc = subprocess.Popen([sys.executable, 'Deleting extra files.py'])
    proc.communicate()

if __name__ == "__main__":
    main()
    
