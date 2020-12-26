from django.urls import path

from news import views as news_views

app_name = 'news'

urlpatterns = [
    path('', news_views.Index.as_view(), name='index'),
    path('<int:id>',news_views.NewsSingle.as_view(),name="news"),
    path('api/news', news_views.News.as_view(), name='newsAPI_get'),
    path('api/news/<int:id>/',news_views.News_Singolo.as_view(),name='newsAPI_article')
]