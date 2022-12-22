import requests
import csv
import concurrent.futures


proxylist = []

with open('proxylist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

def extract(proxy):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        #change the url for what website u want to test on
        r = requests.get('https://rec.net', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=2)
        print(r.json(), ' | Works')
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, proxylist)