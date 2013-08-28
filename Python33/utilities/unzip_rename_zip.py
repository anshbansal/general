import zipfile
import os
import shutil

CUR_DIR = os.getcwd()
FILES_IN_CUR_DIR = os.listdir(CUR_DIR)

def get_new_name(original_name):
    num = 0
    started= False
    for c in original_name[7:]:
        if not c.isdigit():
            if started is True:
                break
            continue
        else:
            started = True
            num *= 10
            num += int(c)
    return str(num).zfill(4) + original_name[4:]


def extract_files(zip_f, cur_path):
    with zipfile.ZipFile(zip_f, 'r') as zip_file:
        zip_file.extractall(cur_path)


def rename_files(cur_path):
    for files in os.listdir(cur_path):
        new_name = get_new_name(files)
        os.rename(os.path.join(cur_path, files),
                  os.path.join(cur_path, new_name))


def main():    
    files = [f for f in FILES_IN_CUR_DIR
             if f.endswith('.zip')]

    for f in files:
        cur_path = os.path.join(CUR_DIR, f[:-4])
        print('Extracting ' + f)
        extract_files(f, cur_path)
        print('Started renaming')
        rename_files(cur_path)
        print('Removing zip file ', f)
        os.remove(os.path.join(CUR_DIR, f))
        print('Writing back to ' + f)
        shutil.make_archive(cur_path, 'zip', cur_path)
        print('\n')


if __name__ == "__main__":
    main()
