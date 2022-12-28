import requests
import pandas as pd 

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

""" baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

r = requests.get(baseurl + endpoint)

#print(r.json())

data = r.json() """

# https://rickandmortyapi.com/api/character/?page=19

def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl + endpoint + f'?page={x}')
    return r.json()

#pages = data['info']['pages'] #instead of this line of code we could create a method get_pages
def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    charlist = []
    for item in response['results']:
        #print(item['name'], len(item['episode']))
        char = {
            'id': item['id'],
            'name': item['name'],
            'no_ep':len(item['episode']),
        }
        charlist.append(char)
    return charlist

mainlist = []
data = main_request(baseurl, endpoint, 1)
for x in range(1, get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(baseurl, endpoint, x)))

#print(len(mainlist))

df = pd.DataFrame(mainlist)

#print(df.head(), df.tail())

df.to_csv('charlist.csv', index=False)




#print(parse_json(data))

#numOfPages = get_pages(data)

#namesEpisodes = parse_json(data)
#print(namesEpisodes) #ovo daje none kad parse_json ne vraca listu
#print(numOfPages)
#print(len(episodes))
#print(name)

