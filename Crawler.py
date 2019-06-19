import time
import urllib
import bs4
import requests
start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    article_link = None
    for element in soup.find_all('p'):
        if element.find('a'):
            article_link = element.find("a").get('href')
            print(article_link)
            break
        
    if not article_link:
        return
    
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    return first_link

def continue_crawl(search_history, target_url):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("Stuck in a loop!")
        return False
    else:
        return True

article_chain = [start_url]
count = 0
while continue_crawl(article_chain, target_url):
    count = count + 1
    print('count: ', count)
    first_link = find_first(article_chain[-1])
    if not first_link:
        print("No links exist here!")
        break

    article_chain.append(first_link)
    time.sleep(0.5)
