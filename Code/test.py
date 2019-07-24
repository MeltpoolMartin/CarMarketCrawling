import re

url = 'https://www.autoscout24.de/lst/audi/q5?sort=standard&desc=0&gear=A&fuel=B&ustate=N%2CU&size=20&page=1' \
      '&powerfrom=147&powertype=hp&cy=D&kmto=10000&kmfrom=0&fregfrom=2018&atype=C&'

page_expr = re.compile(r'page=\d')
mo_page = page_expr.search(url)
print(mo_page.group())

km_expr = re.compile((r'kmto=\d\d\d\d\d&kmfrom=\d\d\d\d\d|\d'))
mo_km = km_expr.search(url)
print(mo_km.group())

delta_page = 3

for page in range(delta_page):
    print(url.replace(mo_page.group(),'page=' + str(page)))