import os
import shutil
import zipfile

FOLDER_SET = 8
FOLDER_NUM_LEN = 4


def folder_sets(dir_names):
    extra_folders = len(dir_names) % FOLDER_SET
    if extra_folders != 0:
        folders_to_be_zipped = dir_names[:-extra_folders]
    else:
        folders_to_be_zipped = dir_names
    for i in range(0, len(folders_to_be_zipped), FOLDER_SET):
        yield folders_to_be_zipped[i: i + FOLDER_SET]


def make_zips(dir_path, dir_names):
    for folders in folder_sets(dir_names):
        archive_name = os.path.join(dir_path, folders[0][:FOLDER_NUM_LEN] + "-" + folders[-1][:FOLDER_NUM_LEN] + ".zip")
        with zipfile.ZipFile(archive_name, "w", zipfile.ZIP_DEFLATED) as z:
            for folder in folders:
                for i in os.listdir(os.path.join(dir_path, folder)):
                    z.write(os.path.join(dir_path, folder, i), os.path.join(folder, i))
            else:
                for folder in folders:
                    shutil.rmtree(os.path.join(dir_path, folder))

def filter_directories(dir_names):
    for directory in dir_names:
        if directory.endswith("_Read"):
            return [directory]
    return dir_names

def main():
    for dir_path, dir_names, file_names in os.walk('.'):
        dir_names[:] = filter_directories(dir_names)
        if dir_path.endswith("_Read"):
            make_zips(dir_path, dir_names)


if __name__ == "__main__":
    main()
