#! python3
import helper

FILE_NAME = 'my_blog_stats_file.txt'
CURRENT_URL = 'http://www.alexa.com/search?q=anshbansal.wordpress.com&r=site_screener&p=bigtop'
FLAG = '/siteinfo/anshbansal.wordpress.com#trafficstats'

def parse_line(line):
    """This separates the stat-name and associated number"""
    ans = 0
    for c in line:
        if '0' <= c <= '9':
            ans *= 10
            ans += int(c)
    return str(ans)

def parse(url_handle):
    flags = 0
    next_line = False
    for line in url_handle:
        temp_line = str(line)[2:-5]
        if next_line == True:
            return parse_line(temp_line)

        if FLAG in temp_line:
            flags += 1
            if flags == 3:
                next_line = True

def main():
    if helper.already_written(FILE_NAME):
        return

    data, url_handle, today = helper.write_helper(
        FILE_NAME, CURRENT_URL)

    data[0] = today + '\n'
    data.append(today + ',' + parse(url_handle) + '\n')
    with open(FILE_NAME, 'w') as f:
        f.writelines(data)


if __name__ == "__main__":
    main()
