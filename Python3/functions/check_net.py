import urllib.request

def internet_on():
    try:
        response = urllib.request.urlopen('http://google.com', timeout = 20)
        return True
    except:
        return False
