import urllib.request
import re

url = "https://www.google.com/search?q=PATIL+EYE+CARE&kgmid=/g/11vrz87p3j"
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
)

try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8', errors='ignore')
        # Print basic snippets or matching patterns for phone, address
        print("Length of HTML:", len(html))
        
        # Let's extract title
        title = re.search(r'<title>(.*?)</title>', html)
        if title:
            print("Title:", title.group(1))
            
        # Let's search for some text around "Patil" or "Address" or "Phone"
        # We can extract text inside tags or look for typical Indian phone numbers or address structures
        # Find all occurrences of phone numbers
        phones = re.findall(r'\+91\s*\d{5}\s*\d{5}|\b\d{10}\b|\b\d{5}\s*\d{5}\b', html)
        print("Potential Phone Numbers:", list(set(phones))[:10])
        
        # Let's print out text that looks like a clinic address or doctor name
        # We can print some clean text lines
        text_lines = []
        for line in html.split('\n'):
            clean = re.sub(r'<[^>]+>', ' ', line).strip()
            clean = re.sub(r'\s+', ' ', clean)
            if clean and any(kw in clean.lower() for kw in ["patil", "eye", "care", "clinic", "road", "street", "hospital", "doctor"]):
                text_lines.append(clean)
                
        print("\n--- Snippets found ---")
        for line in text_lines[:30]:
            print(line[:150])
            
except Exception as e:
    print("Error:", e)
