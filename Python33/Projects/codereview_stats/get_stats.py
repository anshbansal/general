#! python3
import urllib.request
import datetime

FILE_NAME = 'data_file.txt'
CURRENT_URL = 'http://codereview.stackexchange.com/'

def today_date():
    return datetime.date.today().strftime('%d-%m-%Y')


def already_written():
    with open(FILE_NAME, 'a+') as f:
        f.seek(0)
        first_line = f.readline()
        if today_date() == first_line[:-1]:
            return True
        return False


def parse(line):
    """This separates the stat-name and associated number"""
    temp = [0, '']
    braces = False
    for c in line:
        if c == '<':
            braces = True
        elif c == '>':
            braces = False
        elif braces is True or c in [' ', ',', '%']:
            continue
        elif c.isdigit():
            temp[0] *= 10
            temp[0] += int(c)
        else:
            temp[1] += c

    return temp


def write_stats():
    '''This writes the stats into the file'''
    with open(FILE_NAME, 'r') as f:
        data = f.readlines()

    with open(FILE_NAME, 'w') as f:
        f.write(today_date() + '\n')
        f.writelines(data[1:])

        url_handle = urllib.request.urlopen(CURRENT_URL)
        write_this = today_date() + ','
        for line in url_handle:
            temp_line = str(line)[2:-5]
            if 'stats-value' in temp_line and 'label' in temp_line:
                temp = parse(temp_line)
                write_this += str(temp[0]) + ','
        else:
            write_this += '\n'
            f.write(write_this)

def main():
    if not already_written():
        write_stats()

if __name__ == "__main__":
    main()
