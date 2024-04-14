import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text,'html.parser')

links =soup.select('.titleline >a')
#.titleline > a
#print(links)

subtext = soup.select('.subtext')

#print(votes)
def sort_stories_by_votes(stories):
  return sorted(stories, key= lambda k:k['points'],reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for inx, item in enumerate(links):
    title = links[inx].getText()
    href = links[inx].get('href', None)
    vote = subtext[inx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points',''))
      if points>=100:
        hn.append({'title': title, 'link': href, 'points': points})
  return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))
