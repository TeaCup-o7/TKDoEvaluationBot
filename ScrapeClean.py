from numpy.lib.shape_base import split
import requests
from bs4 import BeautifulSoup
import Search_Parse as sp

def PullData(input):
    print("Starting HTML scrape.")
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

    user_index = 'http://users.nexustk.com/userfiles/'

    #scrape page
    user_scrape = requests.get(user_index + input + ".html", headers = headers)
    user_soup = BeautifulSoup(user_scrape.content, 'html.parser')
    table = user_soup.find('table')
    table = table.get_text()
    split = table.split('\n')
    i = 0
    while (i < len(split)):
        try:
            split.remove('')
            i = i + 1
        except:
            i = i + 1000
    charData = split[0]
    charData = charData.split(' ')
    charName = charData[1]
    charRank = charData[0]
    legend = split.index("Legend")
    legend = split[legend+2:]
    print("End HTML scrape with charName: {}, charRank: {}, legend (uncomment) returned to calling method.".format(charName, charRank))
    return(charName, charRank, legend)