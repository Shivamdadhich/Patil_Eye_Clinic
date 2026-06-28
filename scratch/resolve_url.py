import urllib.request

url = "https://share.google/TOm2CBVf1P7brA9rt"
try:
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    )
    with urllib.request.urlopen(req) as response:
        print("Final URL:", response.geturl())
except Exception as e:
    print("Error:", e)
