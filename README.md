# DNS-GFWlist
A project aimed at building a GFWlist of DNS pollution by exploring polluted DNS data.

## Project Description

1. The inception of this project was solely for the purpose of a "Computer Network Course" experiment. The creator of this project strictly adheres to the stipulations outlined in the "Computer Information Network International Internet Security Protection Management Measures."
2. As a result of employing less sophisticated request methods, long-term stable querying isn't guaranteed. However, the project was functioning normally as of December 11, 2020.
3. The testing environment was the Nanjing University campus network. Upon testing, it was found that the level of DNS pollution and DNS attacks on the campus were relatively mild, with the results far less than the records in GFWlist.
4. The PowerPoint slides for the class sharing are also stored in the root directory of this project.
5. The focus of this project is purely technical. It does not involve personal emotions or seek to infer the author's position.

## How to Use

Install the dependencies:

```python
pip install -r requirements.txt
```

Run main.py

## Technical Implementation

### Motivation:

1. Upon continuous attempts to request [www.google.com](http://www.google.com/), it was observed that the IP addresses returned by DNS are few and the same.

2. If the incorrect IP addresses returned by DNS are queried in reverse, other polluted websites can be found. (This only applies to DNS reverse queries within China, overseas DNS reverse query APIs are not effective.)

### Search Method:

First, a set of initial websites is specified (selecting those that are heavily attacked by DNS), and a dictionary is initialized with a large weight.

Several iterations are performed:

- Select the website with the current highest weight from the dictionary.
- Conduct a DNS request for the website and perform a reverse query.
- If the request is indeed attacked, the weights of all websites found in the reverse query in the dictionary are increased by one.

Return the updated dictionary in descending order.

### Python Packages Used

- `requests`: Constructs requests for IP reverse queries on IP138.
- `beautifulsoup4`: Processes the requested data.
- `dnspython`: Performs DNS requests for websites.
- `python_Levenshtein`: Calculates the edit distance between the domain name string of the request and the domain name list obtained through the IP reverse query to filter out unpolluted DNS query results.

## Future Possibilities

1. Classify the obtained websites (perhaps a new way to acquire the latest adult content domain names? But this may not carry much significance).
2. Analyze the DNS pollution situation across different regions and service providers.
