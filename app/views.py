from django.http import response
import requests
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):

    

    
    site = 'https://api.allnigerianewspapers.com.ng/api'
    news = requests.get(f'{site}/allnews/')
    news = news.json()


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
    sport = response.json()


    response = requests.get(f'http://api.allnigerianewspapers.com.ng/api/allnewsbycategory/politics')
    politics = response.json()
    

  
   

    context = {"allnews": allnews, "category": category, "news": news, "site": site, "headlines": headlines, "sport": sport, "politics": politics}
    return render(request, "home.html", context)



def NewsByCategory(request, category):
    category = requests.get(f'http://api.allnigerianewspapers.com.ng/api/allnewsbycategory/{category}')
    newscategory = category.json()
    context = {"newscategory": newscategory}

    return render(request, "news_bycategory.html", context)
 


def NewsBySites(request, site):
    response = requests.get(f'http://api.allnigerianewspapers.com.ng/api/newsbymedia/{site}')
    newssite = response.json()
    context = {"newssite", newssite}
    return render(request, "news_bysite.html", context)



def NewsDetails(request, id):
    
    response = requests.get(f'http://api.allnigerianewspapers.com.ng/api/newsdetails/{id}')
    print(response)
    newsdetails = response.json()
    context = {"newsdetails", newsdetails}
    return render(request, "news_details.html", context)
