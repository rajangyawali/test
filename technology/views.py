from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from itertools import chain
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parser
import pandas as pd
from . models import AllNews, TechNews, TelcoNews, GadgetNews, GlobalNews, NewsPost
from . news import (prabidhi_technews, prabidhi_gadgetnews, ktmpost_technews, gadgetbyte_technews, 
                    techlekh_technews, nepalitelecom_technews, nepalitelecom_telconews, nepalitelecom_gadgetnews,
                    techsathi_technews, techsathi_gadgetnews)
from . clustering import cluster


PAGINATION_NUMBER = 10

# Create your views here.
def home(request):
    tech_news = TechNews.objects.all()[:4]
    telco_news = TelcoNews.objects.all()[:4]
    gadget_news = GadgetNews.objects.all()[:4]
    global_news = GlobalNews.objects.all()[:4]
    context = {
        'tech_news':tech_news,
        'telco_news':telco_news,
        'gadget_news':gadget_news,
        'global_news':global_news,
    }
    return render(request, 'technology/home.html', context)

def recentNews(request):
    headlines = cluster(newsclass = 'technews')
    tech_news = []
    for h in headlines:
        headlines_cluster = []
        for headline in h:
            headlines_cluster.append(TechNews.objects.get(title=headline))
        tech_news.append(headlines_cluster)
    
    paginator = Paginator(tech_news, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        tech_news = paginator.page(page)
    except(EmptyPage, InvalidPage):
        tech_news = paginator.page(1)

    index = tech_news.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'tech_news':tech_news,
        'page_range':page_range,
    }
    return render(request, 'technology/recentnews.html', context)

def telcoNews(request):
    headlines = cluster(newsclass = 'telconews')
    telco_news = []
    for h in headlines:
        headlines_cluster = []
        for headline in h:
            headlines_cluster.append(TelcoNews.objects.get(title=headline))
        telco_news.append(headlines_cluster)
    
    paginator = Paginator(telco_news, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        telco_news = paginator.page(page)
    except(EmptyPage, InvalidPage):
        telco_news = paginator.page(1)

    index = telco_news.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'telco_news':telco_news,
        'page_range':page_range,
    }
    return render(request, 'technology/telconews.html', context)

def gadgetNews(request):
    headlines = cluster(newsclass = 'gadgetnews')
    gadget_news = []
    for h in headlines:
        headlines_cluster = []
        for headline in h:
            headlines_cluster.append(GadgetNews.objects.get(title=headline))
        gadget_news.append(headlines_cluster)
    
    paginator = Paginator(gadget_news, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        gadget_news = paginator.page(page)
    except(EmptyPage, InvalidPage):
        gadget_news = paginator.page(1)

    index = gadget_news.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'gadget_news':gadget_news,
        'page_range':page_range,
    }
    return render(request, 'technology/gadgetnews.html', context)

def globalNews(request):
    headlines = cluster(newsclass = 'globalnews')
    global_news = []
    for h in headlines:
        headlines_cluster = []
        for headline in h:
            headlines_cluster.append(GlobalNews.objects.get(title=headline))
        global_news.append(headlines_cluster)
    
    paginator = Paginator(global_news, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        global_news = paginator.page(page)
    except(EmptyPage, InvalidPage):
        global_news = paginator.page(1)

    index = global_news.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'global_news':global_news,
        'page_range':page_range,
    }
    return render(request, 'technology/globalnews.html', context)

def searchNews(request):
    news_list = AllNews.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        news_list = news_list.filter(Q(title__icontains = search_query) | Q(description__icontains = search_query))
        paginator = Paginator(news_list, PAGINATION_NUMBER)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1
        try:
            news_list = paginator.page(page)
        except:
            news_list = paginator.page(1)

        index = news_list.number - 1
        max_index = 10
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]

    else:
        news_list = []
        page_range = 1

    context = {
        'news_list':news_list,
        'page_range':page_range,
        'search_query':search_query,
    }
    return render(request, 'technology/searchnews.html', context)

def samsungNews(request):
    search_query = 'samsung'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(description__icontains = search_query))

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/samsungnews.html', {'news_list':news_list})

def huaweiNews(request):
    search_query = 'huawei'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(description__icontains = search_query))

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/huaweinews.html', {'news_list':news_list})

def xiaomiNews(request):
    search_query = 'xiaomi'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(description__icontains = search_query))

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/xiaominews.html', {'news_list':news_list})

def oppoNews(request):
    search_query = 'oppo'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(description__icontains = search_query))

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/opponews.html', {'news_list':news_list})

def vivoNews(request):
    search_query = 'vivo'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(description__icontains = search_query))

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/vivonews.html', {'news_list':news_list})

def appleNews(request):
    search_query = 'apple'
    search_query1 = 'macbook'
    search_query2 = 'iphone'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(description__icontains = search_query) |
                                            Q(title__icontains = search_query) | Q(description__icontains = search_query) |
                                            Q(title__icontains = search_query) | Q(description__icontains = search_query))

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/applenews.html', {'news_list':news_list})

def laptopNews(request):
    search_query = 'laptop'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(description__icontains = search_query))

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/laptopnews.html', {'news_list':news_list})

def NTCNews(request):
    search_query = 'ntc'
    search_query1 = 'nepal telecom'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(description__contains = search_query) |
                                            Q(title__icontains = search_query1) | Q(description__contains = search_query1))

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/ntcnews.html', {'news_list':news_list})

def SmartCellNews(request):
    search_query = 'smart cell'
    search_query1 = 'smart telecom'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(description__icontains = search_query) |
                                            Q(title__icontains = search_query1) | Q(description__icontains = search_query1))

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/smartcellnews.html', {'news_list':news_list})

def NcellNews(request):
    search_query = 'axiata'
    search_query1 = 'ncell'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(description__icontains = search_query) |
                                            Q(title__icontains = search_query1) | Q(description__icontains = search_query1))

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/ncellnews.html', {'news_list':news_list})

def NTANews(request):
    search_query = 'nta'
    search_query1 = 'nepal telecommunication authority'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(description__icontains = search_query) |
                                            Q(title__icontains = search_query1) | Q(description__icontains = search_query1))

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/ntanews.html', {'news_list':news_list})

def LTENews(request):
    search_query = 'lte'
    search_query1 = '4g'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(title__icontains = search_query1) )

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/ltenews.html', {'news_list':news_list})

def FiveGNews(request):
    search_query = '5G'
    search_query1 = 'fifth generation'
    news_list = AllNews.objects.all().filter(Q(title__icontains = search_query) | Q(title__icontains = search_query1) )

    paginator = Paginator(news_list, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news_list = paginator.page(1)

    index = news_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'news_list':news_list,
        'page_range':page_range,
    }
    return render(request, 'technology/fivegnews.html', {'news_list':news_list})

def getNews(request):
        
    technews = prabidhi_technews()
    for data in technews.itertuples():
        try:
            TechNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = 'Prabidhi News')
        except:
            print('Error fetching Tech News from Prabidhi')
    for data in technews.itertuples():
        try:
            AllNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = 'Prabidhi News')
        except:
            print('Error fetching Tech News from Prabidhi')

    gadgetnews = prabidhi_gadgetnews()
    for data in gadgetnews.itertuples():
        try:        
            GadgetNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = 'Prabidhi News')
        except:
            print('Error fetching Gadget News from Prabidhi')
    for data in gadgetnews.itertuples():
        try:        
            AllNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = 'Prabidhi News')
        except:
            print('Error fetching Gadget News from Prabidhi')

    technews = ktmpost_technews()
    for data in technews.itertuples():
        try:
            GlobalNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5])
        except:
            print('Error fetching Global News from Kathmandu Post')
    for data in technews.itertuples():
        try:
            AllNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5])
        except:
            print('Error fetching Global News from Kathmandu Post')

    technews = gadgetbyte_technews()
    for data in technews.itertuples():
        try:            
            TechNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6])
        except:
            print('Error fetching Tech News from Gadgetbyte')
    for data in technews.itertuples():
        try:            
            AllNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6])
        except:
            print('Error fetching Tech News from Gadgetbyte')

    technews = techlekh_technews()
    for data in technews.itertuples():
        try:        
            TechNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6])
        except:
            print('Error fetching Tech News from Techlekh')
    for data in technews.itertuples():
        try:        
            AllNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6])
        except:
            print('Error fetching Tech News from Techlekh')

    technews = nepalitelecom_technews()
    for data in technews.itertuples():
        try:
            TechNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6])
        except:
            print('Error fetching Tech News from Nepali Telecom')
    for data in technews.itertuples():
        try:
            AllNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6])
        except:
            print('Error fetching Tech News from Nepali Telecom')

    telconews = nepalitelecom_telconews()
    for data in telconews.itertuples():
        try:        
            TelcoNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6])
        except:
            print('Error fetching Telecom News from Nepali Telecom')
    for data in telconews.itertuples():
        try:        
            AllNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6])
        except:
            print('Error fetching Telecom News from Nepali Telecom')

    gadgetnews = nepalitelecom_gadgetnews()
    for data in gadgetnews.itertuples():
        try:            
            GadgetNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6])
        except:
            print('Error fetching Gadget News from Nepali Telecom')
    for data in gadgetnews.itertuples():
        try:            
            AllNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6])
        except:
            print('Error fetching Gadget News from Nepali Telecom')

    technews = techsathi_technews()
    for data in technews.itertuples():
        try:        
            TechNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = 'Tech Sathi', posted = data[6])
        except:
            print('Error fetching Tech News from Tech Sathi ')
    for data in technews.itertuples():
        try:
            AllNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = 'Tech Sathi', posted = data[6])
        except:
            print('Error fetching Tech News from Tech Sathi ')

    gadgetnews = techsathi_gadgetnews()
    for data in gadgetnews.itertuples():
        try:            
            GadgetNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = 'Tech Sathi', posted = data[6])
        except:
            print('Error fetching Gadget News from Tech Sathi')
    for data in gadgetnews.itertuples():
        try:            
            AllNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = 'Tech Sathi', posted = data[6])
        except:
            print('Error fetching Gadget News from Tech Sathi')

    return render(request, 'technology/getnews.html',{})

def error_404(request, exception):
    return render(request, 'error_404.html', status='404')

def error_500(request):
    return render(request, 'error_500.html', status='500')
