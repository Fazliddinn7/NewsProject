from django.urls import path
from .views import news_list, news_detail, ContactPageView, HomePageView, notFound ,\
    LocalNewsView, FogiegnNewsView, SportNewsView, TexnologyNewsView


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('404page/', notFound, name='404page'),
    path('local/', LocalNewsView.as_view(), name='local_news_page'),
    path('foreign/', FogiegnNewsView.as_view(), name='foreign_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
    path('texnologiya/', TexnologyNewsView.as_view(), name='technology_news_page'),
]
