import MarkFinder as mf
import requests
from bs4 import BeautifulSoup



def level_test(nameIn): #fetches the user's level if not avail.
    print("Starting special check: {} is 99 or not.".format(nameIn))
    level = 0
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

    user_index = 'http://users.nexustk.com/webreport/Do.htm'

    user_scrape = requests.get(user_index, headers = headers)
    user_soup = BeautifulSoup(user_scrape.content, 'html.parser')
    
    soup_select = user_soup.get_text()
    split_soup = soup_select.splitlines()

    pos = 0
    try:
        while pos < len(split_soup):
            split_soup.remove('')
            pos = pos + 1
    except:
        pos = pos + 10000
    status, mark = mf.Mark_Test(split_soup, (nameIn))
    print(mark)
    mark_split = mark[0].split(' ')
    level = mark_split[6].split(')')
    print('Ending special check: {} is {}'.format(nameIn,level[0]))
    return (level[0])

def LifeOfBreath(rank, name):
    print("Starting Life of Breath test.")
    LBC = 0
    level = 0
    if rank == 'Do':
        level = level_test(name)
        try:
            level = level_test(name)
        except :
            pass #oh well
    if rank == "HwarangDo":  
        LBC = LBC + 2
        level = 99
    elif rank == "Sulsa-Do":
        LBC = LBC + 3
        level = 99
    elif rank == "Jeong-Do" or rank == "Jung-Do":
        LBC = LBC + 4
        level = 99
    elif rank == "Wonhwa":
        LBC = LBC + 5
        level = 99
    elif int(level) == 99:
        LBC = 1
        level = 99
    print("Ending Life of Breath test with level: {} and points: {} returned to calling method.".format(level, LBC))
    return(level, LBC)
