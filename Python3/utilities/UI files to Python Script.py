#TODO Placed in Python3 without running. Don't have Qt installed
#Convert .ui files created by QtCreator to .py files
#The .py files are for use with PySide

#Use
#Either run it through IDLE or simple double-click it

import os
import sys

def only_this_dir(directory):
    #For all .ui files in this directory 
    #returns name.ui
    return [f for f in os.listdir(directory)
            if os.path.isfile(f) and f.endswith('.ui')]

def all_dir(directory):
    #For all .ui files in this directory and sub-directories
    #returns relative_path/name.ui
    ans = []
    for path, folders, files in os.walk(directory):
        for f in files:
           if f.endswith('.ui'):
               ans.append( os.path.relpath(os.path.join(path, f)))
    return ans

def ui_to_py(directory):
    ui_files = all_dir(directory)
    for files in ui_files:
        argument = os.path.dirname(sys.executable) +\
                   '\\Scripts\\pyside-uic.exe -o ' +\
                   files[: - len('.ui')] + '_python.py ' +\
                   files
        
        os.system(argument)       

ui_directory = '.\\..\\..\\Qt_workspace'
ui_to_py(ui_directory)
