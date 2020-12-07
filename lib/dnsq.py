import dns.resolver

def dns_query(domain):
    ips = []
    A = dns.resolver.query(domain,'A')
    for i in A.response.answer:
        for j in i.items:
            if (j.rdtype == 1):
                ips.append(j.address)
    return ips 