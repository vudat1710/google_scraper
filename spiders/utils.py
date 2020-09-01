import json
from tldextract import extract

def load_proxies(filename, newpath):
    proxies = json.load(open(filename, "r"))
    proxies = ['{}:{}'.format(x["proxy_address"], x["proxy_port"]) for x in proxies]
    with open(newpath, 'w') as f:
        for i in range(len(proxies)):
            f.write(proxies[i])
            if i != len(proxies) - 1:
                f.write("\n")
    
    return proxies

def check_crawled_url(url, keyword):
    if url:
        if "›" in url:
            url = url.split("›")[0].strip()
        else:
            url = url.strip()
        _, dn, _ = extract(url)
        return (dn in keyword or keyword in dn or dn == "wikipedia"), url
    else: return False, ""
