from django.http import response
import requests
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


# Create your views here.
def home(request):
    site = 'https://api.allnigerianewspapers.com.ng/api'
    new = requests.get(f'{site}/allnews/')
    news = new.json()
    news2 = new.json()[5:28]
    page = request.GET.get('page', 1)
    paginator = Paginator(news, 10)
    try:
        allnews = paginator.page(page)
    except PageNotAnInteger:
        allnews = paginator.page(1)
    except EmptyPage:
        allnews = paginator.page(paginator.num_pages)
    category = requests.get('http://api.allnigerianewspapers.com.ng/api/category/')
    category= category.json()
    site = requests.get('http://api.allnigerianewspapers.com.ng/api/site/')
    site = site.json()
    response = requests.get(f'http://api.allnigerianewspapers.com.ng/api/allnewsbycategory/headline')
    headlines = response.json()
    response = requests.get(f'http://api.allnigerianewspapers.com.ng/api/allnewsbycategory/sport')
    #sport = response.json()
    response = requests.get(f'http://api.allnigerianewspapers.com.ng/api/allnewsbycategory/politics')
    politics = response.json()
    health_news = requests.get(f'http://api.allnigerianewspapers.com.ng/api/allnewsbycategory/health')
    health1 = health_news.json()[3:9]
    health2 = health_news.json()[:2]
    entertainment_news = requests.get(f'http://api.allnigerianewspapers.com.ng/api/allnewsbycategory/entertainment')
    entertainment = entertainment_news.json()
    fashion_news = requests.get(f'http://api.allnigerianewspapers.com.ng/api/allnewsbycategory/fashion')
    fashion = fashion_news.json()
    fashion2 = fashion_news.json()[3:12]
    sport_news = requests.get(f'http://api.allnigerianewspapers.com.ng/api/allnewsbycategory/sport')
    sport1 = sport_news.json()[:2]
    sport2 = sport_news.json()[3:7]
    context = {"news2": news2,"sport2": sport2,"sport1": sport1, "fashion2": fashion2,"fashion": fashion,"entertainment": entertainment, "health1": health1, "health2": health2, "allnews": allnews, "category": category, "news": news, "headlines": headlines, "politics": politics}
    return render(request, "home.html", context)



def NewsByCategory(request, category):
    categorys = requests.get(f'http://api.allnigerianewspapers.com.ng/api/allnewsbycategory/{category}')
    newscategory = categorys.json()
    category_name = category
    page = request.GET.get('page', 1)
    paginator = Paginator(newscategory, 14)
    try:
        cat_site = paginator.page(page)
    except PageNotAnInteger:
        cat_site = paginator.page(1)
    except EmptyPage:
        cat_site = paginator.page(paginator.num_pages)
    context = {"newscategory": cat_site, "category_name": category_name}
    return render(request, "news_bycategory.html", context)
 


def NewsBySites(request, site):
    response = requests.get(f'http://api.allnigerianewspapers.com.ng/api/newsbymedia/{site}')
    newssite = response.json()
    c = []
    for n in newssite:
        c.append(n['category']['name'])
    
    cat = Count('newssite')
    page = request.GET.get('page', 1)
    paginator = Paginator(newssite, 14)
    try:
        news_site = paginator.page(page)
    except PageNotAnInteger:
        news_site = paginator.page(1)
    except EmptyPage:
        news_site = paginator.page(paginator.num_pages)

    site_name = site
    context = {"newssite": news_site, "site_name": site_name, 'cat': cat}
    return render(request, "news_bysite.html", context)



def NewsDetails(request, id):
    response = requests.get(f'http://api.allnigerianewspapers.com.ng/api/newsdetails/{id}')
    print(response)
    newsdetails = response.json()
    context = {"newsdetails": newsdetails}
    return render(request, "news_details.html", context)
