num_max_pages = 5
url = 'https://www.autoscout24.de/lst/land-rover/range-rover-evoque?sort=standard&desc=0&eq=140%2C155%2C23&gear=A&fuel=B&ustate=N%2CU&size=10&page=1&powerfrom=147&powertype=hp&cy=D&kmto=50000&fregfrom=2016&ptype=M&atype=C&'
for page in range(0, num_max_pages):
    url = url.replace('page=' + str(page), 'page=' + str(page+1))
    print(url)
