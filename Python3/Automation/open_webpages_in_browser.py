#! python3
import webbrowser
import time

URLS = [
    'http://codereview.stackexchange.com/',
    'http://programmers.stackexchange.com/',
    'http://stackoverflow.com/'
    ]
DELAY = 2

def main():
    for URL in URLS:
        webbrowser.open(URL, 2)
        time.sleep(DELAY)

main()
