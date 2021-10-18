from django.urls import path
from .import views


urlpatterns=[
    path('', views.home, name='index'),

    path('newsbycategory/<str:category>', views.NewsByCategory, name='news_by_category'),

    path('newsbysite/<str:site>', views.NewsBySites, name='news_by_site'),

    path('newsbycategory/<str:category>', views.NewsByCategory, name='news_by_category'),
    
    path('newsbdetails/<int:id>', views.NewsDetails, name='news_details')


      
]