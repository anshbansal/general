#! python3
import helper
from my_blog_constants import FILE_NAME, CURRENT_URL, FLAG

def parse_line(line):
    """This separates the stat-name and associated number"""
    ans = 0
    for c in line:
        if '0' <= c <= '9':
            ans *= 10
            ans += int(c)
    return str(ans)

def parse(url_handle):
    for line in url_handle:
        temp_line = str(line)[2:-5]
        if FLAG == temp_line[:10]:
            return parse_line(temp_line)

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
