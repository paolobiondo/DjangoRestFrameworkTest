from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from news import forms as news_forms
from news import models as news_models

#REST API
from news.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class News(APIView):
    def get(self,request):
        news = news_models.News.objects.all()
        serializer = PostSerializer(news, many=True)
        return Response(serializer.data)

class News_Singolo(APIView):
    def get(self,request,id):
        news = news_models.News.objects.filter(id=id)
        serializer = PostSerializer(news, many=True)
        return Response(serializer.data)

    def delete(self,request,id):
        news = news_models.News.objects.filter(id=id)
        news.delete()
        return HttpResponse('deleted')


class Index(View):
    def get(self, request):
        args = {}
        args['form'] = news_forms.NewsForm()
        return render(request,'index.html',args)

    def post(self, request):
        form = news_forms.NewsForm(request.POST)
        if form.is_valid():
            post = news_models.News()
            post.title=form.cleaned_data['title']
            post.content=form.cleaned_data['content']
            post.save()
            return HttpResponse('thanks')
    