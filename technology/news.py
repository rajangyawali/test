import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

def prabidhi_technews():
    url = 'https://prabidhi.info/en/news/'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    tech_news = soup.find_all('div', {'class' : 'td_block_inner'})
    titles = tech_news[0].find_all('h3', {'class': 'entry-title td-module-title'})
    title = [title.find('a').get_text() for title in titles]

    description = tech_news[0].find_all('div' , {'class':'td-excerpt'})
    description = [desc.get_text()[22:-19] for desc in description]

    url_list = []
    for tag in tech_news[0].find_all('h3', {'class': 'entry-title td-module-title'}):
        for t in tag:
            t.find_all('a', href = True)
            url_list.append(str(t['href']))
            
    image_url_list = []
    image_urls = tech_news[0].find_all('img')
    for url in image_urls:
        url.find_all('img', src = True)
        i = url['srcset'].split(',')[-1].split(' ')[1]
        image_url_list.append(i)

    df = pd.DataFrame({
        'title': title,
        'description' : description,
        'url' : url_list,
        'image_url' : image_url_list
    }, index = None)
    return df

def prabidhi_gadgetnews():
    url = 'https://prabidhi.info/en/category/gadgets/'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    gadget_news = soup.find_all('div', {'class' : 'td-ss-main-content'})

    titles = gadget_news[0].find_all('h3', {'class': 'entry-title td-module-title'})
    title = [title.find('a').get_text() for title in titles]

    description = gadget_news[0].find_all('div' , {'class':'td-excerpt'})
    description = [desc.get_text()[22:-16] for desc in description]

    url_list = []
    for tag in gadget_news[0].find_all('h3', {'class': 'entry-title td-module-title'}):
        for t in tag:
            t.find_all('a', href = True)
            url_list.append(str(t['href']))
            
    image_url_list = []
    image_urls = gadget_news[0].find_all('img')
    for url in image_urls:
        url.find_all('img', src = True)
        i = url['srcset'].split(',')[-1].split(' ')[1]
        image_url_list.append(i)

    df = pd.DataFrame({
        'title': title,
        'description' : description,
        'url' : url_list,
        'image_url' : image_url_list
    }, index = None)
    return df

def ktmpost_technews():
    url = 'https://kathmandupost.com/science-technology'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    tech_news = soup.find_all('div', {'class' : 'block--morenews'})

    titles = tech_news[0].find_all('h3')
    title = [title.get_text() for title in titles]

    descriptions = tech_news[0].find_all('p')
    description = [desc.get_text() for desc in descriptions]

    url_list = []
    for tag in tech_news[0].find_all('figure'):
        for t in tag:
            t.find_all('a')
            url_list.append('https://kathmandupost.com' + t['href'])
            
    image_url_list = []
    for url in tech_news[0].find_all('img'):
        image_url_list.append(str(url))
    image_url_list = [url[43:].split('&')[0] for url in image_url_list]

    authors = tech_news[0].find_all('span',{'class':'article-author'})
    author = [author.find('a').get_text() for author in authors]

    df = pd.DataFrame({
            'title': title,
            'description' : description,
            'url' : url_list,
            'image_url' : image_url_list,
            'author' : author
        }, index = None)

    return df

def gadgetbyte_technews():
    url = 'https://www.gadgetbytenepal.com/'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    tech_news = soup.find_all('div', {'class':'td-ss-main-content td_block_template_1'})

    titles = tech_news[0].find_all('h3')
    title = [t.get_text() for t in titles]

    description = tech_news[0].find_all('div' , {'class':'td-excerpt'})
    description = [desc.get_text()[1:] for desc in description]

    url_list = []
    for tag in tech_news[0].find_all('h3'):
        for t in tag:
            t.find_all('a', href = True)
            url_list.append(str(t['href']))
            
    image_url_list = []
    image_urls = tech_news[0].find_all('img')
    for url in image_urls:
        url.find_all('img', src = True)
        i = url['srcset'].split(',')[-1].split(' ')[1]
        image_url_list.append(i)
            
    authors = tech_news[0].find_all('span' , {'class':'td-post-author-name'})
    author = [a.find('a').get_text() for a in authors]

    posted_on = tech_news[0].find_all('span' , {'class':'td-post-date'})
    posted = [p.get_text() for p in posted_on]

    df = pd.DataFrame({
            'title': title,
            'description' : description,
            'url' : url_list,
            'image_url' : image_url_list,
            'author' : author,
            'posted' : posted,
        }, index = None)
    return df

def techlekh_technews():
    url = 'https://techlekh.com/category/gadgets/'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    tech_news = soup.find_all('div', {'class' : 'content-loop blocks clearfix'})

    titles = tech_news[0].find_all('h2', {'class': 'entry-title'})
    title = [title.find('a').get_text() for title in titles]

    descriptions = tech_news[0].find_all('div', {'class':'entry-summary'})
    description = [desc.get_text() for desc in descriptions]

    url_list = []
    for tag in tech_news[0].find_all('h2', {'class' : 'entry-title'}):
        for t in tag:
            t.find_all('a', href = True)
            url_list.append(str(t['href']))
            
    image_url_list = []
    for url in tech_news[0].find_all('img'):
        url.find_all('img', src = True)
        image_url_list.append(str(url['data-orig-file']))
    image_url_list = image_url_list[::2]

    authors = tech_news[0].find_all('span', {'itemprop':'name'})
    author = [author.get_text() for author in authors]

    posted_on = tech_news[0].find_all('a', {'class':'entry-date'})
    posted = [posted.get_text() for posted in posted_on]

    df = pd.DataFrame({
            'title': title,
            'description' : description,
            'url' : url_list,
            'image_url' : image_url_list,
            'author' : author,
            'posted' : posted
        }, index = None)
    return df

def nepalitelecom_technews():
    url = 'https://www.nepalitelecom.com/'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    tech_news = soup.find_all('div', {'class' : 'listing listing-blog listing-blog-5 clearfix columns-1'})

    titles = tech_news[0].find_all('h2',{'class':'title'})
    title = [title.get_text()[2:-1] for title in titles]

    descriptions = tech_news[0].find_all('div',{'class':'post-summary'})
    description = [desc.get_text()[1:-12] for desc in descriptions]

    url_list = []
    for tag in tech_news[0].find_all('a',{'class':'post-title post-url'}):
        url_list.append(tag['href'])
        
    image_url_list = []
    for u in tech_news[0].find_all('a',{'class':'img-holder'}):    
        image_url_list.append(u['data-bsrjs'])
        
    authors = tech_news[0].find_all('div',{'class':'post-meta'})
    author = [author.find('i').get_text() for author in authors]

    posted_on = tech_news[0].find_all('div',{'class':'post-meta'})
    posted = [posted.find('time').get_text() for posted in posted_on]

    df = pd.DataFrame({
            'title': title,
            'description' : description,
            'url' : url_list,
            'image_url' : image_url_list,
            'author' : author,
            'posted' : posted
        }, index = None)
    return df

def nepalitelecom_telconews():
    url = 'https://www.nepalitelecom.com/category/telco-news'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    news = soup.find_all('div', {'class' : 'listing listing-blog listing-blog-5 clearfix'})

    titles = news[0].find_all('h2',{'class':'title'})
    title = [title.get_text()[2:-1] for title in titles]

    descriptions = news[0].find_all('div',{'class':'post-summary'})
    description = [desc.get_text()[1:-12] for desc in descriptions]

    url_list = []
    for tag in news[0].find_all('a',{'class':'post-title post-url'}):
        url_list.append(tag['href'])
        
    image_url_list = []
    for u in news[0].find_all('a',{'class':'img-holder'}):    
        image_url_list.append(u['data-bsrjs'])
        
    authors = news[0].find_all('div',{'class':'post-meta'})
    author = [author.find('i').get_text() for author in authors]

    posted_on = news[0].find_all('div',{'class':'post-meta'})
    posted = [posted.find('time').get_text() for posted in posted_on]

    df = pd.DataFrame({
            'title': title,
            'description' : description,
            'url' : url_list,
            'image_url' : image_url_list,
            'author' : author,
            'posted' : posted
        }, index = None)
    return df

def nepalitelecom_gadgetnews():
    url = 'https://www.nepalitelecom.com/category/gadgets-nepal'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    news = soup.find_all('div', {'class' : 'listing listing-blog listing-blog-5 clearfix'})

    titles = news[0].find_all('h2',{'class':'title'})
    title = [title.get_text()[2:-1] for title in titles]

    descriptions = news[0].find_all('div',{'class':'post-summary'})
    description = [desc.get_text()[1:-12] for desc in descriptions]

    url_list = []
    for tag in news[0].find_all('a',{'class':'post-title post-url'}):
        url_list.append(tag['href'])
        
    image_url_list = []
    for u in news[0].find_all('a',{'class':'img-holder'}):    
        image_url_list.append(u['data-bsrjs'])
        
    authors = news[0].find_all('div',{'class':'post-meta'})
    author = [author.find('i').get_text() for author in authors]

    posted_on = news[0].find_all('div',{'class':'post-meta'})
    posted = [posted.find('time').get_text() for posted in posted_on]

    df = pd.DataFrame({
            'title': title,
            'description' : description,
            'url' : url_list,
            'image_url' : image_url_list,
            'author' : author,
            'posted' : posted
        }, index = None)
    return df

def techsathi_technews():
    url = 'https://techsathi.com/category/news/'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    tech_news = soup.find_all('div', {'class' : 'posts-list listing-alt'})

    titles = tech_news[0].find_all('div', {'class': 'content'})
    title = [title.find('a').get_text()[7:] for title in titles]

    description = tech_news[0].find_all('div' , {'class':'excerpt'})
    description = [desc.find('p').get_text() for desc in description]

    url_list = []
    for url in tech_news[0].find_all('a', {'class':'post-title'}, href = True):
        url_list.append(str(url['href']))
        
    image_url_list = []
    image_urls = tech_news[0].find_all('img')
    for url in image_urls:
        url.find_all('img', src = True)
        i = url['src'].split('?')[0]
        image_url_list.append(i)

    posted_on = tech_news[0].find_all('time')
    posted = [posted.get_text() for posted in posted_on]

    df = pd.DataFrame({
            'title': title,
            'description' : description,
            'url' : url_list,
            'image_url' : image_url_list,
            'posted' : posted
        }, index = None)
    return df

def techsathi_gadgetnews():
    url = 'https://techsathi.com/category/gadgets/'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    gadget_news = soup.find_all('div', {'class' : 'row b-row listing meta-below grid-2'})

    titles = gadget_news[0].find_all('h2', {'class': 'post-title'})
    title = [title.find('a').get_text() for title in titles]

    description = gadget_news[0].find_all('div' , {'class':'excerpt'})
    description = [desc.get_text()[:-2] for desc in description]

    url_list = []
    for tag in gadget_news[0].find_all('h2', {'class':'post-title'}):
        for t in tag:
            t.find_all('a', href = True)
            url_list.append(str(t['href']))
            
    image_url_list = []
    image_urls = gadget_news[0].find_all('img')
    for url in image_urls:
        url.find_all('img', src = True)
        i = url['src'].split('?')[0]
        image_url_list.append(i)

    posted_on = gadget_news[0].find_all('time')
    posted = [posted.get_text() for posted in posted_on]

    df = pd.DataFrame({
            'title': title,
            'description' : description,
            'url' : url_list,
            'image_url' : image_url_list,
            'posted' : posted
        }, index = None)
    return df

