from django.urls import path
from . import views

app_name = 'technology'

urlpatterns = [
    path('', views.home, name='home'),
    path('get-news/', views.getNews, name = 'getnews'),
    path('recent-news/', views.recentNews, name = 'recentnews'),
    path('telco-news/', views.telcoNews, name = 'telconews'),
    path('gadget-news/', views.gadgetNews, name = 'gadgetnews'),
    path('global-news/', views.globalNews, name = 'globalnews'),
    path('samsung/', views.samsungNews, name = 'samsungnews'),
    path('huawei/', views.huaweiNews, name = 'huaweinews'),
    path('oppo/', views.oppoNews, name = 'opponews'),
    path('vivo/', views.vivoNews, name = 'vivonews'),
    path('apple/', views.appleNews, name = 'applenews'),
    path('xiaomi/', views.xiaomiNews, name = 'xiaominews'),
    path('laptops/', views.laptopNews, name = 'laptopnews'),
    path('nepal-telecom/', views.NTCNews, name = 'ntcnews'),
    path('ncell/', views.NcellNews, name = 'ncellnews'),
    path('smart-cell/', views.SmartCellNews, name = 'smartcellnews'),
    path('lte-4G/', views.LTENews, name = 'ltenews'),
    path('5G/', views.FiveGNews, name = 'fivegnews'),
    path('NTA/', views.NTANews, name = 'ntanews'),
    path('search/', views.searchNews, name = 'searchnews'),
]
