import json

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
        if "http" in url:
            url = url.split("://")[1]
            if "www" in url:
                dn = url.split(".")[1]
            else:
                dn = url.split(".")[0]
        else:
            dn = url.split(".")[0]
        return (dn in keyword or dn == "wikipedia"), url
    else: return False, ""
