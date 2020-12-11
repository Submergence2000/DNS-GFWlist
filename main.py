from lib.bs4_ip import getip138, pollution_verify
from lib.dnsq import dns_query
import queue

if __name__ == "__main__":
    domain_dict = {"www.google.com":10, "www.twitter.com":10, "www.facebook.com":10, "cn.nytimes.com":10, "www.epochtimes.com":10, "www.t66y.com":10, "www.pixiv.net":10, "www.bbc.com":10, "www.reddit.com":11}
    domain_unsearch = list(domain_dict.keys())
    ip_visited = []
    for i in range(0,200):
        gen_domain = domain_unsearch[0]

        for key in domain_unsearch:
            if (domain_dict[key] > domain_dict[gen_domain]):
                gen_domain = key
        domain_unsearch.remove(gen_domain)
        for ip in dns_query(gen_domain):
            if ip in ip_visited:
                continue
            else:
                ip_visited.append(ip)
            print(ip)
            rev_domains =  pollution_verify(gen_domain, getip138(ip, "ip"))
            for rev_domain in rev_domains:
                domain_unsearch.append(rev_domain)
                if (rev_domain in domain_dict.keys()):
                    domain_dict[rev_domain] += 1
                else:
                    domain_dict[rev_domain] = 1

    print(sorted(domain_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=1))