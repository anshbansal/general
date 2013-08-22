#! python3
import urllib.request
import datetime


def parse(line):
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


def write_stats(filehandle):
    with open('test.txt', 'a') as f:
        f.write(datetime.date.today().strftime('%d-%m-%Y')
                + '\n\n')

        for line in filehandle:
            temp_line = str(line)[2:-5]
            if 'stats-value' in temp_line and 'label' in temp_line:
                temp = parse(temp_line)
                f.write(temp[1] + ' ' + str(temp[0]) + '\n')

        f.write('\n')


def main():
    filehandle = urllib.request.urlopen(
        'http://codereview.stackexchange.com/')
    write_stats(filehandle)
    filehandle.close()

main()
