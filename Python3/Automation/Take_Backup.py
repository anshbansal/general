import os
import datetime_ab

RESOURCES = "Resources"


def registry_user_variable():
    file_name = os.path.join(RESOURCES, 'user_variables_' + datetime_ab.today() + '.reg')
    os.system('regedit /e ' + file_name + ' "HKEY_CURRENT_USER\\Environment"')


def take_registry_backup():
    registry_user_variable()


def start_task(task):
    print(task[1] + " START")
    task[0]()
    print(task[1] + " END")

if __name__ == "__main__":
    TASKS = [(take_registry_backup, "Registry Backup")]
    for task in TASKS:
        start_task(task)