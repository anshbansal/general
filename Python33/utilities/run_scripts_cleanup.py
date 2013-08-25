import sys
import subprocess

theproc = subprocess.Popen([sys.executable,
                            "Deleting extra files.py"])
theproc.communicate()
