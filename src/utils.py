import urllib.request

def download(url: str, path: str):
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36")]
    urllib.request.install_opener(opener)

    urllib.request.urlretrieve(
        url=url, 
        filename=path
    )