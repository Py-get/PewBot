import grequests
url = input("Input url: ")
urllist = [url] * 100
while True:
    req = [grequests.get(url, stream=True) for urls in urllist]
    response = grequests.map(req)
