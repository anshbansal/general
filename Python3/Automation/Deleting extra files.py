#! python3

#Part of my automatation for managing my code content
#Cleans up my offline C git repository
#Deletes unneeded files from the repository
import os

def delete_or_not(name):
    extensions = ['.exe', '.o']
    for i in extensions:
        if name.endswith(i):
            return True
        
    return False

def cur_files(files):
    for name in files:
        if delete_or_not(name):
            yield name

def main(startpath):
    exclude = ['.git']
    for path, folders, files in os.walk(startpath, True):
        for folder in exclude:
            if folder in folders:
                folders.remove(folder)
                
        for name in cur_files(files):
            os.remove(path + "\\" + name)
    
main(os.getcwd() + "\\..\\..\\C\\")
main(os.getcwd() + "\\..\\..\\Cpp\\")
