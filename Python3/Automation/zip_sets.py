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
        start_num = folders[0][:FOLDER_NUM_LEN]
        archive_name = start_num + "-" + str(int(start_num) + FOLDER_SET - 1).zfill(FOLDER_NUM_LEN) + ".zip"
        with zipfile.ZipFile(os.path.join(dir_path, archive_name), "w", zipfile.ZIP_DEFLATED) as z:
            for folder in folders:
                for i in os.listdir(os.path.join(dir_path, folder)):
                    z.write(os.path.join(dir_path, folder, i), os.path.join(folder, i))
            else:
                for folder in folders:
                    shutil.rmtree(os.path.join(dir_path, folder))


def main():
    for dir_path, dir_names, file_names in os.walk('.'):
        if dir_path.endswith("_Read"):
            make_zips(dir_path, dir_names)


if __name__ == "__main__":
    main()
