from django.shortcuts import render,HttpResponse
from . import models
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.
def article_list(request):
    # get all articles 
    if request.method == "GET":
        articles = models.Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer
        .data, safe=False
        )
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer
        .errors, status=400)
        
def article_details(request, pk):
    try:
        article = models.Article.objects.get(pk=pk)
        
    except models.Article.DoesNotExist :
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = ArticleSerializer(article
        )
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer
        .errors, status=400)
    elif request.method == "DELETE":
        article.delete()
        return HttpResponse(status=204)
            