import requests
from bs4 import BeautifulSoup
import re
import Levenshtein

def getip138(url, url_type):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Connection': 'keep-alive',
        'Referer': 'http://www.baidu.com/'
    }
    ip138_url = "https://site.ip138.com/"
    re_pattern_ip = re.compile(r'<li><span class="date">.*</span><a href=.* target="_blank">(.*)</a></li>')
    re_pattern_domain = re.compile(r'<p>.<span class="date">.*</span>.<a href=.* target="_blank">(.*)</a>.</p>', re.DOTALL)
    req_count = 0
    while(True): 
        r = requests.get(ip138_url + url ,headers = headers)
        req_count = req_count + 1
        if(r.status_code==200):
            break
        if(req_count > 5):
            print("未能成功请求:"+url)
            return []
    
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "html.parser")

    if (url_type == "ip"):
        org_links = soup.find_all('li')
    elif (url_type == "domain"):
        org_links = soup.find_all('p')
    
    links = []
    for org_link in org_links:
        org_link = str(org_link)
        if(url_type == "ip"):
            if(len(re_pattern_ip.findall(org_link))):
                links.append(re_pattern_ip.findall(org_link)[0])
        elif(url_type== "domain"):
            if(len(re_pattern_domain.findall(org_link))):
                links.append(re_pattern_domain.findall(org_link)[0])
    return links

def pollution_verify(domain, rev_domains):
    similar_count = 0
    for rev_domain in rev_domains:
        dist = Levenshtein.distance(domain, rev_domain)
        if dist < (abs(len(rev_domain) - len(domain)) + 0.25*(min(len(rev_domain), len(domain)))):
            rev_domains.remove(rev_domain)
            similar_count = similar_count + 1
    
    if similar_count > 0.1*len(rev_domains):
        return []
    else:
        return rev_domains
    