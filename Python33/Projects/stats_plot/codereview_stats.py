#! python3
import helper

FILE_NAME = 'data_file.txt'
CURRENT_URL = 'http://codereview.stackexchange.com/'

def parse_line(line):
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

def parse(url_handle):
    write_this = ''
    with open(FILE_NAME, 'r') as f:
        for line in url_handle:
            temp_line = str(line)[2:-5]
            if ('stats-value' in temp_line and
                'label' in temp_line):
                temp = parse_line(temp_line)
                write_this += str(temp[0]) + ','
    return write_this

def main():
    if not helper.already_written(FILE_NAME):
        data, url_handle, today = helper.write_helper(
            FILE_NAME, CURRENT_URL)

        with open(FILE_NAME, 'w') as f:
            f.write(today + '\n')
            f.writelines(data[1:])
            f.write(today + ',' + parse(url_handle) + '\n')

if __name__ == "__main__":
    main()
