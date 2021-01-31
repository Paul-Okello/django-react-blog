from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import ArticleSerializer
from .models import Article



class ArticleList(APIView):
    
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer
        .errors, status=status.HTTP_400_BAD_REQUEST)
        

class ArticleDetails(APIView):
    
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        articles = self.get_object(id)
        serializer = ArticleSerializer(articles)
        
        return Response(serializer.data)
    
    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=204)