import datetime
import urllib.request

def today_date():
    return datetime.date.today().strftime('%d-%m-%Y')

def already_written(file_name):
    with open(file_name, 'a+') as f:
        f.seek(0)
        first_line = f.readline()
        if today_date() == first_line[:-1]:
            return True
        return False

def write_helper(file_name, url):
    with open(file_name, 'r') as f:
        data = f.readlines()
        url_handle = urllib.request.urlopen(url)

    return data, url_handle, today_date()
