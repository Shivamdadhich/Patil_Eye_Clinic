import urllib.request

url = "https://patil-eye-clinic.vercel.app/static/style.css"
try:
    with urllib.request.urlopen(url) as response:
        print("Status code:", response.status)
        print("Content length:", response.getheader('Content-Length'))
except Exception as e:
    print("Error:", e)
