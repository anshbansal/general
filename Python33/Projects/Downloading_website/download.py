#! python3
import urllib.request

def download_pages():
    filehandle = urllib.request.urlopen(
        'http://www.cplusplus.com/reference/clibrary/')
    with open('test.html', 'w+b') as f:
        for line in filehandle:
            f.write(line)

    filehandle.close()

def main():
    download_pages()
    #Code for parsing the HTML

main()
