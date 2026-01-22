import re
import urllib.request
import matplotlib.pyplot as plt
from urllib.request import Request, urlopen

req = Request('https://en.wikipedia.org/wiki/Erwin_Schr%C3%B6dinger',
             headers = {'User-Agent':'Mozilla/5.0'})
hand = urlopen(req)

years = []

for line in hand:
    line = line.decode().strip()
    if re.search('academictree.org.', line):
        break
    years_result19 = re.findall('19[0-9]{2}', line)
    years_result20 = re.findall('20[0-2][0-6]', line)
    if years_result19 != []:
        years += years_result19
    if years_result20 != []:
        years += years_result20

int_years = []
for i in years:
    int_years.append(int(i))


plt.hist(int_years, bins=60, color='green', edgecolor='black')
plt.xlabel('Years in Article')
plt.title('Times Years Appeared in Wikipedia Article for Schroedinger')


plt.show()
plt.savefig('bruh.png', dpi=200)

