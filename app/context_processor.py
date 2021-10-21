from django.http import response
import requests
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_constant_data(request):
    allcategorys = requests.get('http://api.allnigerianewspapers.com.ng/api/category/')
    category= allcategorys.json()
    sites = requests.get('http://api.allnigerianewspapers.com.ng/api/site/')
    site = sites.json()
    recent_news = requests.get('https://api.allnigerianewspapers.com.ng/api/allnews/')
    recent = recent_news.json()[5:22]
    postNext = recent_news.json()[:1]
    postPrevious = recent_news.json()[2:3]

    return{
        'site':site,
        'category':category,
        'recent':recent,
        'postNext': postNext,
        'postPrevious': postPrevious,
    }