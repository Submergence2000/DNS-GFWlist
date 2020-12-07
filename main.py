from lib.bs4_ip import getip138, pollution_verify
from lib.dnsq import dns_query
import queue

if __name__ == "__main__":
    domain = queue.Queue()
    init_domain = "www.google.com"
    for ip in dns_query(init_domain):
        print(ip)
        rev_domains =  pollution_verify(init_domain, getip138(ip, "ip"))
        for rev_domain in rev_domains:
            domain.put(rev_domain)

    while not domain.empty():
        print(domain.get())